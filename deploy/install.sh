#!/bin/bash

set -euo pipefail

SKIP_CONFIRM=false

DEFAULT_PROJECT_NAME="botmanager"
DEFAULT_DOMAIN="botmanager.site"
PYTHON_BIN="python3"  # Можно заменить на python3.10 или др.

# Логирование с timestamp
log() {
  echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"
}

# Проверка, что скрипт запускается от root или через sudo
if [[ $EUID -ne 0 ]]; then
  log "❗ Скрипт должен быть запущен с правами root или через sudo"
  exit 1
fi

# Обработка аргументов
while [[ $# -gt 0 ]]; do
  case "$1" in
    --yes|-y) SKIP_CONFIRM=true; shift ;;
    --domain) DOMAIN="$2"; shift 2 ;;
    --project) PROJECT_NAME="$2"; shift 2 ;;
    *) log "❌ Неизвестный аргумент: $1"; exit 1 ;;
  esac
done

# Запрос PROJECT_NAME, если не передан
if [ -z "${PROJECT_NAME-}" ]; then
  read -rp "Введите название проекта [${DEFAULT_PROJECT_NAME}]: " input
  PROJECT_NAME="${input:-$DEFAULT_PROJECT_NAME}"
fi

# Запрос DOMAIN, если не передан
if [ -z "${DOMAIN-}" ]; then
  read -rp "Введите домен [${DEFAULT_DOMAIN}]: " input
  DOMAIN="${input:-$DEFAULT_DOMAIN}"
fi

PROJECT_DIR="/var/www/$PROJECT_NAME"
WEBHOOK_DIR="/opt/webhook"
NGINX_CONF="/etc/nginx/sites-available/$DOMAIN"
NGINX_ENABLED="/etc/nginx/sites-enabled/$DOMAIN"
WEBHOOK_SYSTEMD_SERVICE="/etc/systemd/system/webhook.service"
WEBAPP_SYSTEMD_SERVICE="/etc/systemd/system/webapp.service"

confirm() {
  if [ "$SKIP_CONFIRM" = false ]; then
    read -rp "$1 (y/n): " answer
    case "$answer" in
      y|Y) return 0 ;;
      *) log "❌ Отменено пользователем."; exit 1 ;;
    esac
  fi
}

log "-------------------------------"
log "Используется проект: $PROJECT_NAME"
log "Используется домен: $DOMAIN"
log "-------------------------------"

# Проверяем наличие rsync, tree
command -v rsync >/dev/null 2>&1 || { log "❌ Пожалуйста, установите rsync."; exit 1; }
command -v tree >/dev/null 2>&1 || { log "❌ Пожалуйста, установите tree."; exit 1; }

log "Структура проекта для копирования:"
tree -L 4 -a -I '__pycache__|*.pyc|*.pyo|venv|.git' ../ | head -n 40

confirm "Выполнить действие: Копирование проекта в $PROJECT_DIR?"

log "📁 Копирую проект в $PROJECT_DIR"
mkdir -p "$PROJECT_DIR"
rsync -a --delete --exclude 'venv' --exclude '__pycache__' --exclude '*.pyc' --exclude '*.pyo' --exclude '.git' ../ "$PROJECT_DIR/"

log "-------------------------------"

confirm "Выполнить действие: Установка зависимостей проекта?"

log "🚀 Устанавливаю зависимости проекта"
cd "$PROJECT_DIR"
$PYTHON_BIN -m venv botmanager_venv
source botmanager_venv/bin/activate
pip install --upgrade pip
if [ ! -f requirements.txt ]; then
  log "❌ requirements.txt не найден в $PROJECT_DIR"
  deactivate
  exit 1
fi
pip install -r requirements.txt
deactivate
log "-------------------------------"

confirm "Выполнить действие: Настройка вебхуков?"

log "📦 Настраиваю вебхуки"
mkdir -p "$WEBHOOK_DIR"
if [ ! -f ./webhook/webhook_listener.py ]; then
  log "❌ Файл webhook_listener.py не найден в ./webhook/"
  exit 1
fi
cp ./webhook/webhook_listener.py "$WEBHOOK_DIR/"

confirm "Выполнить действие: Установка зависимостей webhook_venv?"

log "🚀 Устанавливаю зависимости webhook_venv"
cd "$WEBHOOK_DIR"
$PYTHON_BIN -m venv webhook_venv
source webhook_venv/bin/activate
pip install --upgrade pip
if [ ! -f webhook_requirements.txt ]; then
  log "❌ webhook_requirements.txt не найден в $WEBHOOK_DIR"
  deactivate
  exit 1
fi
pip install -r webhook_requirements.txt
deactivate
log "-------------------------------"

confirm "Выполнить действие: Настройка systemd-сервиса webhook?"

log "🔧 Настраиваю systemd-сервис webhook"
if [ ! -f ./systemd/webhook.service ]; then
  log "❌ webhook.service не найден в ./webhook/"
  exit 1
fi
cp ./webhook/webhook.service "$WEBHOOK_SYSTEMD_SERVICE"

log "⚙️ Включение и перезапуск webhook.service"
systemctl daemon-reload
systemctl enable webhook.service
systemctl restart webhook.service
log "-------------------------------"

confirm "Выполнить действие: Установка сервиса webapp.service?"

log "🔧 Настраиваю systemd-сервис webapp"
if [ ! -f ./systemd/webapp.service ]; then
  log "❌ webapp.service не найден в текущей директории"
  exit 1
fi
cp ./webapp.service "$WEBAPP_SYSTEMD_SERVICE"

log "⚙️ Включение и перезапуск webapp.service"
systemctl daemon-reload
systemctl enable webapp.service
systemctl restart webapp.service
log "-------------------------------"

confirm "Выполнить действие: Настройка nginx?"

log "🔧 Настраиваю nginx"
cat > "$NGINX_CONF" << EOF
server {
    listen 443 ssl;
    server_name $DOMAIN www.$DOMAIN;

    ssl_certificate /etc/letsencrypt/live/$DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/$DOMAIN/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    root /var/www/$PROJECT_NAME/static;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }

    location /static/ {
        alias /var/www/$PROJECT_NAME/app/static/;
        expires off;
        add_header Cache-Control "no-store, no-cache, must-revalidate, proxy-revalidate, max-age=0";
    }
}

server {
    listen 80;
    server_name $DOMAIN www.$DOMAIN;

    return 301 https://\$host\$request_uri;
}
EOF

log "Создан Nginx конфиг: $NGINX_CONF"
log "Содержимое:"
cat "$NGINX_CONF"

if [ ! -L "$NGINX_ENABLED" ]; then
  ln -s "$NGINX_CONF" "$NGINX_ENABLED"
  log "Символическая ссылка создана: $NGINX_ENABLED"
else
  log "Символическая ссылка уже существует: $NGINX_ENABLED"
fi

log "-------------------------------"

confirm "Выполнить действие: Получение SSL через certbot?"

log "🔒 Получаю SSL через certbot"
apt update
apt install -y certbot python3-certbot-nginx
certbot --nginx -d "$DOMAIN" -d "www.$DOMAIN" --non-interactive --agree-tos -m tw44400@gmail.com
log "-------------------------------"

confirm "Выполнить действие: Перезапуск nginx и systemd?"

log "✅ Перезапускаю nginx и systemd"
systemctl restart nginx
systemctl daemon-reload
log "-------------------------------"

log "🎉 Готово! Сайт доступен на https://$DOMAIN"
