#!/bin/bash

# Файл логов
LOG_FILE="/var/log/deploy.log"

# Функция для вывода сообщений одновременно в терминал и лог
log() {
    echo -e "$1" | tee -a "$LOG_FILE"
}

log "===== DEPLOY START: $(date) ====="
log "👤 Скрипт выполняется от пользователя: $(whoami)"

# Пути
PROJECT_DIR="/var/www/tokenguard"
SERVICE_NAME="tokenguard"
GIT_BRANCH="design-update"  # корректное имя ветки

# Переход в директорию проекта
log "📁 Переход в директорию $PROJECT_DIR"
cd "$PROJECT_DIR" || { log "❌ Ошибка: не удалось перейти в $PROJECT_DIR"; exit 1; }

# Проверка ветки и обновление
log "📥 Получение обновлений из git..."
git fetch origin || log "⚠️ Ошибка git fetch, продолжаем..."
if git show-ref --verify --quiet "refs/remotes/origin/$GIT_BRANCH"; then
    git reset --hard "origin/$GIT_BRANCH" || log "⚠️ Ошибка git reset, продолжаем..."
else
    log "⚠️ Ветка origin/$GIT_BRANCH не найдена, пропускаем git reset"
fi

# Очистка неотслеживаемых файлов, кроме исключений
log "🧹 Очистка untracked файлов (venv, .env и т.д. сохраняются)"
git clean -fd -e tokenguard_venv -e .env -e .git -e .gitignore -e deploy.sh || log "⚠️ Ошибка git clean, продолжаем..."

# Перезапуск сервиса
log "🔁 Перезапуск сервиса $SERVICE_NAME..."
if systemctl restart "$SERVICE_NAME"; then
    log "✅ Сервис $SERVICE_NAME успешно перезапущен"
else
    log "❌ Ошибка при перезапуске сервиса $SERVICE_NAME"
    exit 1
fi

log "✅ DEPLOY FINISHED: $(date)"
