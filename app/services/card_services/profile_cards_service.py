def get_profile_cards(user):
    return [

        {
            'type': 'text_info',
            'title': f'Профиль',
            "title_class": "auth-title",
            'content': 'Это карточка вашего личного профиля.',
            'icon': 'house-user',
            'wrapper_class': 'card-info',
            'card_class': 'card-profile',
            'buttons': [],
            'position': 'center'
        }
    ]