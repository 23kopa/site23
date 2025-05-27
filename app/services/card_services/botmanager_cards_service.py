# app/services/dashboard_cards_service.py
from app.services.server_services.systemctl_service import get_cpu_cores
from app.services.server_services.ssh_service import ssh_execute


def get_botmanager_cards():
    return [

        {
            'type': 'text_info',
            'title': 'Скоро...',
            "title_class": "base-title",
            'content': 'В разработке.',
            'icon': 'info-circle',
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
            'icon': 'info-circle',
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
            'icon': 'info-circle',
            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',
            'buttons': [],
            'position': 'grid'
        },
        {
            'type': 'cpu_usage',
            'title': 'Загрузка CPU',
            "title_class": "base-title",
            'content': 'В разработке.',
            'icon': 'microchip',
            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',
            'buttons': [],
            'position': 'grid'
        },
        {
            'type': 'cpu_cores',
            'title': 'Физ. ядра',
            "title_class": "base-title",
            'content': 'В разработке.', # 'content': f'{get_cpu_cores()[0]}',
            'icon': 'microchip',
            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',
            'buttons': [],
            'position': 'grid'
        },
        {
            'type': 'nginx',
            'title': 'Состояние Nginx',
            "title_class": "base-title",
            'content': 'В разработке.', #
            'icon': 'server',
            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',
            'buttons': [],
            'position': 'grid'
        }
    ]
