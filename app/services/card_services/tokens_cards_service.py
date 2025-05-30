# app/services/dashboard_cards_service.py
def get_tokens_cards():
    return [

        {
            'type': 'text_info',
            'title': 'Web bug',
            "title_class": "base-title",
            
            'icon': 'bug',
            'content': 'Уведомление при открытии URL.',

            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',

            'button_class': 'btn-dashboard',
            'button_text': 'Создать',
            'button_url': '/details',

            'id': 'card1',
            'modal_title': 'Создать токен Web bug',
            'modal_content': '1Подробная информация в модалке',
            'modal_description': 'Получайте уведомление, когда злоумышленник открывает или посещает ваш уникальный URL.',

            'position': 'grid',

            'form_action': '/create_webbug_token',
            'submit_text': 'Создать',
            'fields': [
                {
                    'type': 'email',
                    'name': 'email',
                    'label': 'Email',
                    'description': 'Введите ваш Email для уведомлений:',
                    'required': True
                },
                {
                    'type': 'text',
                    'name': 'alert_message',
                    'label': 'Сообщение',
                    'description': 'Сообщение, которое придёт при срабатывании:',
                    'required': False
                }
            ]
        },
        {
            'type': 'text_info',
            'title': 'QR code',
            "title_class": "base-title",
            
            'icon': 'qrcode',
            'content': 'Уведомление при сканировании QR-кода.',

            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',

            'button_class': 'btn-dashboard',
            'button_text': 'Создать',
            'button_url': '/details',

            'id': 'card2',
            'modal_title': 'Создать токен QR-кода',
            'modal_description': 'Получайте уведомление, когда злоумышленник сканирует или переходит по вашему уникальному QR-коду.',

            'position': 'grid',
            
            'form_action': '/create_qrcode_token',
            'submit_text': 'Создать',
            'fields': [
                {
                    'type': 'email',
                    'name': 'email',
                    'label': 'Email',
                    'description': 'Введите ваш Email для уведомлений',
                    'required': True
                },
                {
                    'type': 'text',
                    'name': 'alert_message',
                    'label': 'Сообщение',
                    'description': 'Сообщение, которое придёт при срабатывании',
                    'required': False
                }
            ]
        },
        {
            'type': 'text_info',
            'title': 'DNS',
            "title_class": "base-title",
            
            'icon': 'network-wired',
            'content': 'Уведомление при DNS-запросе.',

            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',

            'button_class': 'btn-dashboard',
            'button_text': 'Создать',
            'button_url': '/details',

            'id': 'card3',
            'modal_title': 'Создать токен DNS',
            'modal_description': 'Получайте уведомление, когда злоумышленник выполняет запрос разрешения DNS-имени, связанного с вашим ресурсом.',

            'position': 'grid',
            
            'form_action': '/create_dns_token',
            'submit_text': 'Создать',
            'fields': [
                {
                    'type': 'email',
                    'name': 'email',
                    'label': 'Email',
                    'description': 'Введите ваш Email для уведомлений',
                    'required': True
                },
                {
                    'type': 'text',
                    'name': 'alert_message',
                    'label': 'Сообщение',
                    'description': 'Сообщение, которое придёт при срабатывании',
                    'required': False
                }
            ]
        },
        {
            'type': 'text_info',
            'title': 'Microsoft Word',
            "title_class": "base-title",

            'icon': 'file-word',
            'content': 'Уведомление при открытии Word-файла.',

            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',

            'button_class': 'btn-dashboard',
            'button_text': 'Создать',
            'button_url': '/details',

            'id': 'card4',
            'modal_title': 'Создать токен Word',
            'modal_description': 'Получайте уведомление, когда злоумышленник открывает ваш защищённый документ Microsoft Word.',

            'position': 'grid',
            
            'form_action': '/create_msword_token',
            'submit_text': 'Создать',
            'fields': [
                {
                    'type': 'email',
                    'name': 'email',
                    'label': 'Email',
                    'description': 'Введите ваш Email для уведомлений',
                    'required': True
                },
                {
                    'type': 'text',
                    'name': 'alert_message',
                    'label': 'Сообщение',
                    'description': 'Сообщение, которое придёт при срабатывании',
                    'required': False
                }
            ]
        },
        {
            'type': 'text_info',
            'title': 'Microsoft Excel',
            "title_class": "base-title",

            'icon': 'file-excel',
            'content': 'Уведомление при открытии Excel-файла.',
            'wrapper_class': 'card-info',
            'card_class': 'card-dashboard',

            'button_class': 'btn-dashboard',
            'button_text': 'Создать',
            'button_url': '/details',

            'id': 'card5',
            'modal_title': 'Создать токен Excel',
            'modal_description': 'Получайте уведомление, когда злоумышленник открывает ваш защищённый документ Microsoft Excel.',

            'position': 'grid',
            
            'form_action': '/create_msexel_token',
            'submit_text': 'Создать',
            'fields': [
                {
                    'type': 'email',
                    'name': 'email',
                    'label': 'Email',
                    'description': 'Введите ваш Email для уведомлений',
                    'required': True
                },
                {
                    'type': 'text',
                    'name': 'alert_message',
                    'label': 'Сообщение',
                    'description': 'Сообщение, которое придёт при срабатывании',
                    'required': False
                }
            ]
        },
        {
            'type': 'text_info',
            'title': 'Web image',
            "title_class": "base-title",

            'icon': 'server',
            'content': 'Уведомление при просмотре изображения.',

            'wrapper_class': 'image',
            'card_class': 'card-dashboard',

            'button_class': 'btn-dashboard',
            'button_text': 'Создать',
            'button_url': '/details',

            'id': 'card6',
            'modal_title': 'Создать токен изображения',
            'modal_description': 'Получайте уведомление, когда загруженное вами изображение просматривается или загружается кем-либо.',

            'position': 'grid',
            
            'form_action': '/create_image_token',
            'submit_text': 'Создать',
            'fields': [
                {
                    'type': 'email',
                    'name': 'email',
                    'label': 'Email',
                    'description': 'Введите ваш Email для уведомлений',
                    'required': True
                },
                {
                    'type': 'text',
                    'name': 'alert_message',
                    'label': 'Сообщение',
                    'description': 'Сообщение, которое придёт при срабатывании',
                    'required': False
                }
            ]
        }
    ]
