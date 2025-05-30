# app/services/dashboard_cards_service.py
from app.services.server_services.systemctl_service import get_cpu_cores
from app.services.server_services.ssh_service import ssh_execute


def get_botmanager_cards():
    return [

        {
            'type': 'text_info',
            'title': 'Скоро...',
            "title_class": "base-title",
            
            'icon': 'info-circle',
            'content': 'В разработке.',

            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',

            'button_class': 'btn-dashboard',
            'button_text': 'Подробнее',
            'button_url': '/details',

            'id': 'card1',
            'modal_title': '1Заголовок модального окна',
            'modal_content': '1Подробная информация в модалке',

            'position': 'grid'
        },
        {
            'type': 'text_info',
            'title': 'Скоро...',
            "title_class": "base-title",
            
            'icon': 'info-circle',
            'content': 'В разработке.',

            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',

            'button_class': 'btn-dashboard',
            'button_text': 'Подробнее',
            'button_url': '/details',

            'id': 'card2',
            'modal_title': '2Заголовок модального окна',
            'modal_content': '2Подробная информация в модалке',

            'position': 'grid'
        },
        {
            'type': 'text_info',
            'title': 'Скоро...',
            "title_class": "base-title",
            
            'icon': 'info-circle',
            'content': 'В разработке.',

            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',

            'button_class': 'btn-dashboard',
            'button_text': 'Подробнее',
            'button_url': '/details',

            'id': 'card3',
            'modal_title': '3Заголовок модального окна',
            'modal_content': '3Подробная информация в модалке',

            'position': 'grid'
        },
        {
            'type': 'text_info',
            'title': 'Загрузка CPU',
            "title_class": "base-title",

            'icon': 'microchip',
            'content': 'В разработке.',

            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',

            'button_class': 'btn-dashboard',
            'button_text': 'Подробнее',
            'button_url': '/details',

            'id': 'card4',
            'modal_title': '4Заголовок модального окна',
            'modal_content': '4Подробная информация в модалке',

            'position': 'grid'
        },
        {
            'type': 'cpu_cores',
            'title': 'Физ. ядра',
            "title_class": "base-title",

            'icon': 'microchip',
            'content': 'В разработке.', # 'content': f'{get_cpu_cores()[0]}',

            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',

            'button_class': 'btn-dashboard',
            'button_text': 'Подробнее',
            'button_url': '/details',

            'id': 'card5',
            'modal_title': '5Заголовок модального окна',
            'modal_content': '5Подробная информация в модалке',

            'position': 'grid'
        },
        {
            'type': 'text_info',
            'title': 'Состояние Nginx',
            "title_class": "base-title",

            'icon': 'server',
            'content': 'В разработке.', #

            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',

            'button_class': 'btn-dashboard',
            'button_text': 'Подробнее',
            'button_url': '/details',

            'id': 'card6',
            'modal_title': '6Заголовок модального окна',
            'modal_content': '6Подробная информация в модалке',

            'position': 'grid'
        }
    ]
