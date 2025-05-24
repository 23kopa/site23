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


```
botmanager
├─ app
│  ├─ models
│  │  └─ users.py
│  ├─ routes
│  │  ├─ auth_routes.py
│  │  ├─ botmanager_routes.py
│  │  ├─ dashboard_routes.py
│  │  ├─ main_routes.py
│  │  ├─ profile_routes.py
│  │  └─ tokens_routes.py
│  ├─ services
│  │  ├─ ssh_service.py
│  │  ├─ tgbot_service.py
│  │  ├─ user_service.py
│  │  └─ vps_service.py
│  ├─ static
│  │  ├─ css
│  │  │  ├─ style.css
│  │  │  └─ style.css.map
│  │  ├─ images
│  │  │  ├─ avatars
│  │  │  │  ├─ user_1.jpeg
│  │  │  │  └─ user_1.png
│  │  │  ├─ default.png
│  │  │  └─ logo.png
│  │  ├─ js
│  │  │  └─ script.js
│  │  └─ scss
│  │     ├─ backgrounds
│  │     │  └─ _background.scss
│  │     ├─ buttons
│  │     │  ├─ _btn-base.scss
│  │     │  ├─ _btn-cyber.scss
│  │     │  └─ _btn-login.scss
│  │     ├─ cards
│  │     │  ├─ cards-grid
│  │     │  │  ├─ _card-1col.scss
│  │     │  │  ├─ _card-2col.scss
│  │     │  │  ├─ _card-3col.scss
│  │     │  │  ├─ _card-4col.scss
│  │     │  │  └─ _card-5col.scss
│  │     │  └─ cards-type
│  │     │     ├─ _card-base.scss
│  │     │     ├─ _card-main.scss
│  │     │     └─ _card-tokens.scss
│  │     ├─ items
│  │     │  ├─ _console.scss
│  │     │  ├─ _description.scss
│  │     │  ├─ _logo.scss
│  │     │  ├─ _navbar.scss
│  │     │  └─ _table.scss
│  │     ├─ notifications
│  │     │  └─ _copy.scss
│  │     └─ style.scss
│  ├─ templates
│  │  ├─ auth
│  │  │  ├─ edit.html
│  │  │  ├─ login.html
│  │  │  ├─ profile.html
│  │  │  └─ register.html
│  │  ├─ base
│  │  │  ├─ base.html
│  │  │  └─ navbar.html
│  │  ├─ cards
│  │  │  ├─ card-1col.html
│  │  │  ├─ card-2col.html
│  │  │  ├─ card-3col.html
│  │  │  ├─ card-4col.html
│  │  │  └─ card-5col.html
│  │  └─ pages
│  │     ├─ botmanager.html
│  │     ├─ dashboard.html
│  │     ├─ index.html
│  │     ├─ test.html
│  │     ├─ tokens.html
│  │     └─ welcome.html
│  └─ __init__.py
├─ config
│  ├─ base_config.py
│  ├─ dev_config.py
│  ├─ prod_config.py
│  ├─ settings.py
│  └─ __init__.py
├─ instance
│  └─ users.db
├─ migrations
├─ README.md
├─ requirements.txt
├─ run.py
└─ wsgi.py

```
```
botmanager
├─ app
│  ├─ models
│  │  └─ users.py
│  ├─ routes
│  │  ├─ auth_routes.py
│  │  ├─ botmanager_routes.py
│  │  ├─ dashboard_routes.py
│  │  ├─ main_routes.py
│  │  ├─ profile_routes.py
│  │  └─ tokens_routes.py
│  ├─ services
│  │  ├─ ssh_service.py
│  │  ├─ tgbot_service.py
│  │  ├─ user_service.py
│  │  └─ vps_service.py
│  ├─ static
│  │  ├─ css
│  │  │  ├─ style.css
│  │  │  └─ style.css.map
│  │  ├─ images
│  │  │  ├─ avatars
│  │  │  │  ├─ user_1.jpeg
│  │  │  │  └─ user_1.png
│  │  │  ├─ default.png
│  │  │  └─ logo.png
│  │  ├─ js
│  │  │  └─ script.js
│  │  └─ scss
│  │     ├─ backgrounds
│  │     │  └─ _background.scss
│  │     ├─ buttons
│  │     │  ├─ _btn-base.scss
│  │     │  ├─ _btn-cyber.scss
│  │     │  └─ _btn-login.scss
│  │     ├─ cards
│  │     │  ├─ cards-grid
│  │     │  │  ├─ _card-1col.scss
│  │     │  │  ├─ _card-2col.scss
│  │     │  │  ├─ _card-3col.scss
│  │     │  │  ├─ _card-4col.scss
│  │     │  │  ├─ _card-5col.scss
│  │     │  │  └─ _cards_col.scss
│  │     │  └─ cards-type
│  │     │     ├─ _card-base.scss
│  │     │     ├─ _card-main.scss
│  │     │     └─ _card-tokens.scss
│  │     ├─ items
│  │     │  ├─ _console.scss
│  │     │  ├─ _description.scss
│  │     │  ├─ _logo.scss
│  │     │  ├─ _navbar.scss
│  │     │  └─ _table.scss
│  │     ├─ notifications
│  │     │  └─ _copy.scss
│  │     └─ style.scss
│  ├─ templates
│  │  ├─ auth
│  │  │  ├─ edit.html
│  │  │  ├─ login.html
│  │  │  ├─ profile.html
│  │  │  └─ register.html
│  │  ├─ base
│  │  │  ├─ base.html
│  │  │  └─ navbar.html
│  │  ├─ cards
│  │  │  ├─ card-1col.html
│  │  │  ├─ card-2col.html
│  │  │  ├─ card-3col.html
│  │  │  ├─ card-4col.html
│  │  │  ├─ card-5col.html
│  │  │  ├─ columns
│  │  │  │  ├─ column_0.html
│  │  │  │  ├─ column_1.html
│  │  │  │  ├─ column_2.html
│  │  │  │  └─ column_3.html
│  │  │  └─ universal-grid.html
│  │  └─ pages
│  │     ├─ botmanager.html
│  │     ├─ dashboard.html
│  │     ├─ index.html
│  │     ├─ test.html
│  │     ├─ tokens.html
│  │     └─ welcome.html
│  └─ __init__.py
├─ config
│  ├─ base_config.py
│  ├─ dev_config.py
│  ├─ prod_config.py
│  ├─ settings.py
│  └─ __init__.py
├─ instance
│  └─ users.db
├─ migrations
├─ README.md
├─ requirements.txt
├─ run.py
└─ wsgi.py

```
```
botmanager
├─ app
│  ├─ models
│  │  └─ users.py
│  ├─ routes
│  │  ├─ auth_routes.py
│  │  ├─ botmanager_routes.py
│  │  ├─ dashboard_routes.py
│  │  ├─ main_routes.py
│  │  ├─ profile_routes.py
│  │  └─ tokens_routes.py
│  ├─ services
│  │  ├─ ssh_service.py
│  │  ├─ tgbot_service.py
│  │  ├─ user_service.py
│  │  └─ vps_service.py
│  ├─ static
│  │  ├─ css
│  │  │  ├─ style.css
│  │  │  └─ style.css.map
│  │  ├─ images
│  │  │  ├─ avatars
│  │  │  │  ├─ user_1.jpeg
│  │  │  │  └─ user_1.png
│  │  │  ├─ default.png
│  │  │  └─ logo.png
│  │  ├─ js
│  │  │  └─ script.js
│  │  └─ scss
│  │     ├─ backgrounds
│  │     │  └─ _background.scss
│  │     ├─ buttons
│  │     │  ├─ _btn-base.scss
│  │     │  ├─ _btn-cyber.scss
│  │     │  └─ _btn-login.scss
│  │     ├─ cards
│  │     │  ├─ cards-grid
│  │     │  │  ├─ _card-1col.scss
│  │     │  │  ├─ _card-2col.scss
│  │     │  │  ├─ _card-3col.scss
│  │     │  │  ├─ _card-4col.scss
│  │     │  │  ├─ _card-5col.scss
│  │     │  │  └─ _card-col.scss
│  │     │  └─ cards-type
│  │     │     ├─ _card-base.scss
│  │     │     ├─ _card-main.scss
│  │     │     └─ _card-tokens.scss
│  │     ├─ items
│  │     │  ├─ _console.scss
│  │     │  ├─ _description.scss
│  │     │  ├─ _logo.scss
│  │     │  ├─ _navbar.scss
│  │     │  └─ _table.scss
│  │     ├─ notifications
│  │     │  └─ _copy.scss
│  │     └─ style.scss
│  ├─ templates
│  │  ├─ auth
│  │  │  ├─ edit.html
│  │  │  ├─ login.html
│  │  │  ├─ profile.html
│  │  │  └─ register.html
│  │  ├─ base
│  │  │  ├─ base.html
│  │  │  └─ navbar.html
│  │  ├─ cards
│  │  │  ├─ card-1col.html
│  │  │  ├─ card-2col.html
│  │  │  ├─ card-3col.html
│  │  │  ├─ card-4col.html
│  │  │  ├─ card-5col.html
│  │  │  ├─ card-grid.html
│  │  │  └─ columns
│  │  │     ├─ column_0.html
│  │  │     ├─ column_1.html
│  │  │     ├─ column_2.html
│  │  │     └─ column_3.html
│  │  └─ pages
│  │     ├─ botmanager.html
│  │     ├─ dashboard.html
│  │     ├─ index.html
│  │     ├─ test.html
│  │     ├─ tokens.html
│  │     └─ welcome.html
│  └─ __init__.py
├─ config
│  ├─ base_config.py
│  ├─ dev_config.py
│  ├─ prod_config.py
│  ├─ settings.py
│  └─ __init__.py
├─ instance
│  └─ users.db
├─ migrations
├─ README.md
├─ requirements.txt
├─ run.py
└─ wsgi.py

```