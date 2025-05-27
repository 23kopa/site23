def get_dashboard_cards(user):
    return [

        {
            'type': 'text_info',
            'title': f'Общая информация',
            "title_class": "base-title",
            'content': 'Это ваша панель управления. Здесь будут отображаться уведомления и статистика.',
            'icon': 'house-user',
            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',
            'buttons': [],
            'position': 'grid'
        },
        {
            'type': 'text_info',
            'title': 'Напоминания',
            "title_class": "base-title",
            'content': f'У вас {user.reminders_count} активных напоминаний.',
            'icon': 'bell',
            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',
            'buttons': [],
            'position': 'grid'
        },
        {
            'type': 'text_info',
            'title': 'Аккаунт',
            "title_class": "base-title",
            'content': f'Email: {user.email}',
            'icon': 'user',
            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',
            'buttons': [],
            'position': 'grid'
        },
        {
            'type': 'text_info',
            'title': 'Скоро...',
            "title_class": "base-title",
            'content': 'В разработке.',
            'icon': 'tools',
            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',
            'buttons': [],
            'position': 'grid'
        },
        {
            'type': 'text_info',
            'title': 'Скоро...',
            "title_class": "base-title",
            'content': 'В разработке.',
            'icon': 'tools',
            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',
            'buttons': [],
            'position': 'grid'
        },
        {
            'type': 'text_info',
            'title': 'Скоро...',
            "title_class": "base-title",
            'content': 'В разработке.',
            'icon': 'tools',
            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',
            'buttons': [],
            'position': 'grid'
        },

    ]
