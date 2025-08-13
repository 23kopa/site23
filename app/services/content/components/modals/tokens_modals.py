def get_tokens_modals():
    return {
        'security': {
            'modal_title': 'Создать токен Web bug',
            'modal_description': 'Получайте уведомление, когда злоумышленник открывает или посещает ваш уникальный URL.',
            'form_action': '/token_generate/create_web_token',
        },
        'card2': {
            'modal_title': 'Создать токен QR-кода',
            'modal_description': 'Получайте уведомление, когда злоумышленник сканирует или переходит по вашему уникальному QR-коду.',
            'form_action': '/create_qrcode_token',
        },
        'card3': {
            'modal_title': 'Создать токен DNS',
            'modal_description': 'Получайте уведомление, когда злоумышленник выполняет запрос разрешения DNS-имени, связанного с вашим ресурсом.',
            'form_action': '/create_dns_token',
        },
        'card4': {
            'modal_title': 'Создать токен Word',
            'modal_description': 'Получайте уведомление, когда злоумышленник открывает ваш защищённый документ Microsoft Word.',
            'form_action': '/create_msword_token',
        },
        'card5': {
            'modal_title': 'Создать токен Excel',
            'modal_description': 'Получайте уведомление, когда злоумышленник открывает ваш защищённый документ Microsoft Excel.',
            'form_action': '/create_msexcel_token',
        },
        'card6': {
            'modal_title': 'Создать токен изображения',
            'modal_description': 'Получайте уведомление, когда загруженное вами изображение просматривается или загружается кем-либо.',
            'form_action': '/create_image_token',
        },
    }
