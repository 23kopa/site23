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