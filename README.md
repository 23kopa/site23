
```
botmanager
├─ .dockerignore
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
│  │     ├─ dashboard_routes.py
│  │     ├─ profile_routes.py
│  │     └─ tokens_routes.py
│  ├─ services
│  │  ├─ card_services
│  │  │  ├─ dashboard_cards_service.py
│  │  │  ├─ login_cards_service.py
│  │  │  ├─ profile_cards_service.py
│  │  │  ├─ register_cards_service.py
│  │  │  └─ tokens_cards_service.py
│  │  └─ server_services
│  │     ├─ ssh_service.py
│  │     └─ systemctl_service.py
│  ├─ static
│  │  ├─ css
│  │  │  ├─ style.css
│  │  │  └─ style.css.map
│  │  ├─ images
│  │  │  ├─ avatars
│  │  │  ├─ default.png
│  │  │  └─ logo.png
│  │  ├─ js
│  │  │  └─ main.js
│  │  └─ scss
│  │     ├─ abstracts
│  │     │  ├─ functions
│  │     │  ├─ mixins
│  │     │  └─ _index.scss
│  │     ├─ base
│  │     │  ├─ elements
│  │     │  ├─ typography
│  │     │  ├─ utilities
│  │     │  ├─ variables
│  │     │  └─ _index.scss
│  │     ├─ components
│  │     │  ├─ buttons
│  │     │  ├─ cards
│  │     │  │  ├─ card_class
│  │     │  │  │  ├─ card-auth
│  │     │  │  │  ├─ card-dashboard
│  │     │  │  │  └─ card-profile
│  │     │  │  └─ _cards.scss
│  │     │  ├─ features
│  │     │  ├─ forms
│  │     │  ├─ items
│  │     │  ├─ modals
│  │     │  │  └─ modal-base
│  │     │  └─ _index.scss
│  │     ├─ layout
│  │     │  ├─ footer
│  │     │  ├─ grid
│  │     │  ├─ header
│  │     │  ├─ sidebar
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
│  │  │  ├─ profile.html
│  │  │  └─ register.html
│  │  ├─ base
│  │  │  ├─ base.html
│  │  │  ├─ navbar.html
│  │  │  └─ welcome.html
│  │  ├─ components
│  │  │  ├─ cards
│  │  │  │  ├─ auth
│  │  │  │  │  ├─ login_card.html
│  │  │  │  │  ├─ profile_card.html
│  │  │  │  │  └─ register_card.html
│  │  │  │  └─ dashboard
│  │  │  │     ├─ action_card.html
│  │  │  │     └─ static_card.html
│  │  │  └─ modals
│  │  │     └─ action_modal.html
│  │  ├─ macros
│  │  │  └─ __init__.html
│  │  └─ pages
│  │     ├─ dashboard.html
│  │     ├─ edit.html
│  │     └─ tokens.html
│  └─ __init__.py
├─ config
│  ├─ base_config.py
│  ├─ dev_config.py
│  ├─ prod_config.py
│  ├─ settings.py
│  └─ __init__.py
├─ docker-compose.yaml
├─ Dockerfile
├─ instance
│  └─ users.db
├─ migrations
│  ├─ alembic.ini
│  ├─ env.py
│  ├─ README
│  ├─ script.py.mako
├─ README.md
├─ requirements.txt
├─ run.py
└─ wsgi.py

```