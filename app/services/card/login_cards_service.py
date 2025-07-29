def get_login_cards():
    return [
        {
            'type': 'form',
            'title': 'Вход',
            "title_class": "auth-title",
            'form_action': '/login',
            'fields': [
                {'label': 'Логин', 'name': 'username', 'type': 'text'},
                {'label': 'Пароль', 'name': 'password', 'type': 'password'},
            ],
            'btn_class': 'btn-auth',
            'submit_text': 'Войти',
            'bottom_text': 'Нет аккаунта? <a href="/login">Зарегистрируйтесь</a>',
            'wrapper_class': 'card-form',
            'card_class': 'card-auth',
        }
    ]
