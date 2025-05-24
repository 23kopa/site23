def get_register_cards():
    return [
        {
            'type': 'form',
            'title': 'Регистрация',
            "title_class": "auth-title",
            'form_action': '/register',
            'fields': [
                {'label': 'Логин', 'name': 'username', 'type': 'text'},
                {'label': 'E-mail', 'name': 'email', 'type': 'text'},
                {'label': 'Пароль', 'name': 'password', 'type': 'password'},
            ],
            'btn_class': 'btn-auth',
            'submit_text': 'Зарегестрироваться',
            'bottom_text': 'Зарегестрированы? <a href="/login">Авторизируйтесь</a>',
            'wrapper_class': 'card-form',
            'card_class': 'card-auth',
        }
    ]
