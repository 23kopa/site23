
```
botmanager.site
├─ .deploy
│  ├─ install.sh
│  ├─ webapp.service
│  └─ webhook
│     ├─ webhook.service
│     ├─ webhook_listener.py
│     └─ webhook_requirements.txt
├─ app
│  ├─ models
│  │  ├─ reminders.py
│  │  ├─ users.py
│  │  └─ __init__.py
│  ├─ routes
│  │  ├─ index_routes
│  │  │  ├─ auth_routes.py
│  │  │  └─ main_routes.py
│  │  └─ pages_routes
│  │     ├─ botmanager_routes.py
│  │     ├─ dashboard_routes.py
│  │     └─ profile_routes.py
│  ├─ services
│  │  ├─ card_services
│  │  │  ├─ botmanager_cards_service.py
│  │  │  ├─ dashboard_cards_service.py
│  │  │  ├─ login_cards_service.py
│  │  │  ├─ profile_cards_service.py
│  │  │  └─ register_cards_service.py
│  │  └─ server_services
│  │     ├─ ssh_service.py
│  │     └─ systemctl_service.py
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
│  │     │  │  ├─ _auth-container.scss
│  │     │  │  ├─ _content.scss
│  │     │  │  ├─ _html.scss
│  │     │  │  ├─ _navbar.scss
│  │     │  │  └─ _normalize.scss
│  │     │  ├─ typography
│  │     │  │  ├─ _headings.scss
│  │     │  │  ├─ _text.scss
│  │     │  │  └─ _title.scss
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
│  │     │  │  ├─ _btn-auth.scss
│  │     │  │  └─ _btn-cyber.scss
│  │     │  ├─ cards
│  │     │  │  ├─ card_class
│  │     │  │  │  ├─ _card-auth.scss
│  │     │  │  │  ├─ _card-dashboard.scss
│  │     │  │  │  └─ _card-profile.scss
│  │     │  │  ├─ wrapper_class
│  │     │  │  │  └─ _card-info.scss
│  │     │  │  └─ _cards.scss
│  │     │  ├─ forms
│  │     │  │  ├─ _form-base.scss
│  │     │  │  └─ _from-auth.scss
│  │     │  ├─ items
│  │     │  │  ├─ _input.scss
│  │     │  │  ├─ _list-group-item.scss
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
│  │     ├─ themes
│  │     │  ├─ _default.scss
│  │     │  └─ _index.scss
│  │     └─ vendors
│  │        ├─ _bootstrap.scss
│  │        └─ _index.scss
│  ├─ templates
│  │  ├─ auth
│  │  │  ├─ login.html
│  │  │  └─ register.html
│  │  ├─ base
│  │  │  ├─ base.html
│  │  │  ├─ navbar.html
│  │  │  └─ welcome.html
│  │  ├─ macros
│  │  │  ├─ cards
│  │  │  │  ├─ botmanager_cards.html
│  │  │  │  ├─ dashboard_cards.html
│  │  │  │  ├─ login_cards.html
│  │  │  │  ├─ profile_cards.html
│  │  │  │  └─ register_cards.html
│  │  │  ├─ renders
│  │  │  │  ├─ botmanager_render.html
│  │  │  │  ├─ dashboard_render.html
│  │  │  │  ├─ login_render.html
│  │  │  │  ├─ profile_render.html
│  │  │  │  └─ register_render.html
│  │  │  └─ __init__.html
│  │  └─ pages
│  │     ├─ botmanager.html
│  │     ├─ dashboard.html
│  │     ├─ edit.html
│  │     └─ profile.html
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