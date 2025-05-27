# SCSS Map

## abstracts/
  - _functions.scss: SCSS-функции
  - _mixins.scss: общие миксины
## base/
  - typography/: текст
  - utilities/: утилиты (margin, padding, display)
## components/
  - buttons/: все стили кнопок
  - cards/: карточки
  - _forms.scss, _modal.scss: общие формы и модалки
## layout/
  - header/, footer/, sidebar/
## pages/
  - dashboard, botmanager: стили для страниц
## themes/
  - _default.scss: основной стиль/цвета

```
botmanager
├─ app
│  ├─ models
│  │  ├─ reminders.py
│  │  ├─ users.py
│  │  └─ __init__.py
│  ├─ routes
│  │  ├─ auth_routes.py
│  │  ├─ botmanager_routes.py
│  │  ├─ main_routes.py
│  │  ├─ profile_routes.py
│  │  └─ tokens_routes.py
│  ├─ services
│  │  ├─ botmanager_cards_service.py
│  │  ├─ dashboard_service.py
│  │  ├─ default_cards_service.py
│  │  ├─ ssh_service.py
│  │  ├─ tgbot_service.py
│  │  ├─ user_service.py
│  │  └─ vps_service.py
│  ├─ static
│  │  ├─ css
│  │  │  ├─ style.css
│  │  │  └─ style.css.map
│  │  ├─ images
│  │  │  ├─ avatars
│  │  │  │  ├─ user_1.jpeg
│  │  │  │  └─ user_1.png
│  │  │  ├─ default.png
│  │  │  └─ logo.png
│  │  ├─ js
│  │  │  └─ script.js
│  │  └─ scss
│  │     ├─ abstracts
│  │     │  ├─ functions
│  │     │  │  └─ _functions.scss
│  │     │  ├─ mixins
│  │     │  │  └─ _mixins.scss
│  │     │  └─ _index.scss
│  │     ├─ base
│  │     │  ├─ elements
│  │     │  │  ├─ _container.scss
│  │     │  │  ├─ _content.scss
│  │     │  │  ├─ _html.scss
│  │     │  │  ├─ _navbar.scss
│  │     │  │  └─ _normalize.scss
│  │     │  ├─ typography
│  │     │  │  ├─ _headings.scss
│  │     │  │  ├─ _index.scss
│  │     │  │  └─ _text.scss
│  │     │  ├─ utilities
│  │     │  │  ├─ _display.scss
│  │     │  │  ├─ _helpers.scss
│  │     │  │  ├─ _spacing.scss
│  │     │  │  └─ _visibility.scss
│  │     │  ├─ variables
│  │     │  │  ├─ _colors.scss
│  │     │  │  └─ _fonts.scss
│  │     │  └─ _index.scss
│  │     ├─ components
│  │     │  ├─ buttons
│  │     │  │  ├─ _buttons-basic.scss
│  │     │  │  ├─ _buttons-helpers.scss
│  │     │  │  └─ _buttons-primary.scss
│  │     │  ├─ cards
│  │     │  │  ├─ card_class
│  │     │  │  │  ├─ _card-base.scss
│  │     │  │  │  ├─ _card-primary.scss
│  │     │  │  │  ├─ _card-success.scss
│  │     │  │  │  └─ _card-warning.scss
│  │     │  │  ├─ wrapper_class
│  │     │  │  │  └─ _card-info.scss
│  │     │  │  └─ _cards.scss
│  │     │  ├─ items
│  │     │  │  ├─ _forms.scss
│  │     │  │  ├─ _input.scss
│  │     │  │  ├─ _modal.scss
│  │     │  │  └─ _scrollbar.scss
│  │     │  └─ _index.scss
│  │     ├─ layout
│  │     │  ├─ footer
│  │     │  │  └─ _base.scss
│  │     │  ├─ header
│  │     │  │  ├─ _logo.scss
│  │     │  │  └─ _nav.scss
│  │     │  ├─ sidebar
│  │     │  │  ├─ _menu.scss
│  │     │  │  └─ _widgets.scss
│  │     │  └─ _index.scss
│  │     ├─ main.scss
│  │     ├─ pages
│  │     │  └─ _index.scss
│  │     ├─ themes
│  │     │  ├─ _default.scss
│  │     │  └─ _index.scss
│  │     └─ vendors
│  │        ├─ _bootstrap.scss
│  │        └─ _index.scss
│  ├─ templates
│  │  ├─ auth
│  │  │  ├─ edit.html
│  │  │  ├─ login.html
│  │  │  ├─ profile.html
│  │  │  └─ register.html
│  │  ├─ base
│  │  │  ├─ base.html
│  │  │  └─ navbar.html
│  │  ├─ macros
│  │  │  ├─ cards
│  │  │  │  ├─ botmanager
│  │  │  │  │  └─ botmanager_card.html
│  │  │  │  └─ dashboard
│  │  │  │     └─ dashboard_card.html
│  │  │  ├─ renders
│  │  │  │  ├─ botmanager_render.html
│  │  │  │  ├─ dashboard_render.html
│  │  │  │  └─ default_render.html
│  │  │  └─ __init__.html
│  │  └─ pages
│  │     ├─ botmanager.html
│  │     ├─ dashboard.html
│  │     ├─ default.html
│  │     ├─ index.html
│  │     ├─ tokens.html
│  │     └─ welcome.html
│  └─ __init__.py
├─ config
│  ├─ base_config.py
│  ├─ dev_config.py
│  ├─ prod_config.py
│  ├─ settings.py
│  └─ __init__.py
├─ instance
│  └─ users.db
├─ migrations
├─ README copy.md
├─ README.md
├─ requirements.txt
├─ run.py
└─ wsgi.py

```