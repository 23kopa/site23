def get_home_header():
    return {
        "title": "Добро пожаловать!",
        "lead_text": (
            "Быстрая и надёжная фиксация событий безопасности с использованием современных "
            "web-технологий и хранилища Redis."
        ),
        "buttons": [
            {
                "text": "Сгенерировать",
                "class": "btn btn-primary btn-lg px-4 shadow",
                "data_bs_toggle": "modal",
                "data_bs_target": "#tokenSelectModal"
            },
            {
                "text": "Документация",
                "href": "#tokens",
                "class": "btn btn-outline-light btn-lg px-4 shadow-sm"
            },
        ],
        "image": {
            "src": "images/gif/homegif.gif",
            "alt": "homegif",
            "class": "img-fluid rounded-4 my-5 shadow-sm",
        },
    }


def get_feature_cards():
    return [
        {
            "icon": "diagram-3",
            "title": "Разделённая логика",
            "description": "Генерация, хранение и срабатывание разделены по модулям.",
        },
        {
            "icon": "database",
            "title": "Redis-хранилище",
            "description": "Токены и события сохраняются в Redis как JSON-объекты.",
        },
        {
            "icon": "code-slash",
            "title": "UID и шаблоны",
            "description": "Токену присваивается UID, URL формируется по шаблону.",
        },
        {
            "icon": "geo-alt",
            "title": "Геолокация клиента",
            "description": "ip-api.com возвращает страну, город и провайдера по IP.",
        },
        {
            "icon": "files",
            "title": "Множество форматов",
            "description": "Токены можно выводить в различных форматах.",
        },
        {
            "icon": "arrow-repeat",
            "title": "Webhook-деплой",
            "description": "Webhook запускает systemd unit после коммитов в GitHub.",
        },
        {
            "icon": "window",
            "title": "Веб-интерфейс Flask",
            "description": "Панель с авторизацией построена на Flask и Bootstrap.",
        },
        {
            "icon": "boxes",
            "title": "Без SQL-монолита",
            "description": "Логика разбита по типам, данные хранятся в Redis.",
        },
    ]


def get_testimonial():
    return {
        "text": (
            "Working with Start Bootstrap templates has saved me tons of development time when building new projects! "
            "Starting with a Bootstrap template just makes things easier!"
        ),
        "author_name": "Tom Ato",
        "author_role": "CEO, Pomodoro",
        "author_image": "https://dummyimage.com/40x40/ced4da/6c757d",
    }
