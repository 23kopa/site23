## botmanager.site (timeweb.cloud)

> Домен зарегистрирован, оплачен до 29 апреля 2026

### Основные функции:

* Авторизация с БД, регистрация
* Личный кабинет: редактирование информации и аватара
* Страница 1 — Управление системой:

  * Управление Telegram-ботом на VPS (systemctl: start, stop, reload)
  * Информация о CPU: использование, частота, ядра
  * Статус Nginx, запуск/остановка
  * Сетевая информация: передано/получено, IP-адреса
* Страница 2 — Honey-токены: карточки токенов (реализация в процессе)
* Страница 3 — Личный кабинет:

  * Отображение аватара, логина, почты
  * Страница редактирования: логин, почта, пароль, аватар

---

### 🌐 Инфраструктура и домен

* **Домен:** botmanager.site (Timeweb Cloud)
* **DNS:**

  * `A` записи:

    * botmanager.site → 185.22.172.242
    * [www.botmanager.site](http://www.botmanager.site) → 185.22.172.242

---

### ⚙️ Веб-сервер

* **Nginx** — реверс-прокси для Flask:

  * SSL от Let's Encrypt
  * Редирект HTTP → HTTPS
  * Обработка статики и кеширование

---

### 🔐 SSL / HTTPS

* **Let's Encrypt + Certbot**:

  * Автообновление сертификатов
  * Команда: `sudo certbot certificates`
  * Конфиги: `/etc/letsencrypt/...`

---

### 🐍 Flask Web App

* **Фреймворк:** Flask
* **Структура проекта:**

  * `app/` — логика и шаблоны
  * `config/` — dev/prod конфиги
  * `.env` — переменные среды
  * `run.py` — точка входа
* **WSGI:** Gunicorn, запускается через systemd

---

### 🧱 Frontend

* Jinja2 шаблоны (auth, base, cards, pages)
* SCSS/CSS по блокам (buttons, cards, items)
* JavaScript: `static/js/script.js`
* Изображения: `static/images/`

---

### 📁 База данных

* **SQLite** — файл: `instance/users.db`

---

### 🛠️ DevOps

* **Systemd unit:** `botmanager.service`

  * Gunicorn + virtualenv
  * Пользователь: www-data

---

### 🧩 Инструменты

* **virtualenv** — `venv/` в `/var/www/botmanager/`
* **dotenv** — переменные среды из `.env`

---

### Структура проекта (путь: `/var/www/botmanager/`):

```
botmanager/
├── .env
├── run.py
├── config/
│   ├── settings.py
│   ├── base_config.py
│   ├── dev_config.py
│   └── prod_config.py
├── app/
│   ├── __init__.py
│   ├── models/
│   │   └── users.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── botmanager_routes.py
│   │   ├── dashboard_routes.py
│   │   ├── main_routes.py
│   │   └── profile_routes.py
│   ├── services/
│   │   ├── ssh_service.py
│   │   ├── tgbot_service.py
│   │   ├── user_service.py
│   │   └── vps_service.py
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   │   └── scss/
│   └── templates/
│       ├── auth/
│       ├── base/
│       ├── cards/
│       └── pages/
├── instance/
│   └── users.db
└── requirements.txt
```

---

### Пример конфигурации systemd (`/etc/systemd/system/botmanager.service`):

```ini
[Unit]
Description=Gunicorn instance to serve botmanager Flask app
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/botmanager
Environment="FLASK_ENV=production"
EnvironmentFile=/var/www/botmanager/.env
ExecStart=/var/www/botmanager/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:5000 run:app

[Install]
WantedBy=multi-user.target
```

---

### Конфигурация Nginx (`/etc/nginx/sites-available/botmanager.site`):

```nginx
server {
    listen 443 ssl;
    server_name botmanager.site www.botmanager.site;

    ssl_certificate /etc/letsencrypt/live/botmanager.site/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/botmanager.site/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    root /var/www/botmanager/static;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /var/www/botmanager/static/;
        expires 30d;
        add_header Cache-Control "public, max-age=2592000";
    }
}

server {
    listen 80;
    server_name botmanager.site www.botmanager.site;
    return 301 https://$host$request_uri;
}
```
