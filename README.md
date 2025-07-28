
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
│  │  │  │  ├─ user_1.jpeg
│  │  │  │  └─ user_1.png
│  │  │  ├─ default.png
│  │  │  └─ logo.png
│  │  ├─ js
│  │  │  ├─ cpu.js
│  │  │  ├─ disk.js
│  │  │  ├─ main.js
│  │  │  ├─ matrix.js
│  │  │  ├─ network.js
│  │  │  ├─ nginx.js
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
│  │     │  │  ├─ _btn-cyber.scss
│  │     │  │  └─ _btn-theme.scss
│  │     │  ├─ cards
│  │     │  │  ├─ card_class
│  │     │  │  │  ├─ card-auth
│  │     │  │  │  │  ├─ _card-auth-bottomtext.scss
│  │     │  │  │  │  ├─ _card-auth-button.scss
│  │     │  │  │  │  ├─ _card-auth-placeholder.scss
│  │     │  │  │  │  ├─ _card-auth-title.scss
│  │     │  │  │  │  └─ _card-auth.scss
│  │     │  │  │  ├─ card-dashboard
│  │     │  │  │  │  ├─ _card-dashboard-button.scss
│  │     │  │  │  │  ├─ _card-dashboard-text.scss
│  │     │  │  │  │  ├─ _card-dashboard-title.scss
│  │     │  │  │  │  └─ _card-dashboard.scss
│  │     │  │  │  └─ card-profile
│  │     │  │  │     └─ _card-profile.scss
│  │     │  │  └─ _cards.scss
│  │     │  ├─ features
│  │     │  ├─ forms
│  │     │  │  ├─ _form-base.scss
│  │     │  │  └─ _from-auth.scss
│  │     │  ├─ items
│  │     │  │  └─ _scrollbar.scss
│  │     │  ├─ modals
│  │     │  │  └─ modal-base
│  │     │  │     ├─ _modal-base-backdrop.scss
│  │     │  │     ├─ _modal-base-body.scss
│  │     │  │     ├─ _modal-base-button.scss
│  │     │  │     ├─ _modal-base-close.scss
│  │     │  │     ├─ _modal-base-description.scss
│  │     │  │     ├─ _modal-base-placeholder.scss
│  │     │  │     ├─ _modal-base-title.scss
│  │     │  │     └─ _modal-base.scss
│  │     │  └─ _index.scss
│  │     ├─ layout
│  │     │  ├─ footer
│  │     │  │  ├─ _base.scss
│  │     │  │  └─ _index.scss
│  │     │  ├─ grid
│  │     │  │  ├─ _index.scss
│  │     │  │  └─ _settings.scss
│  │     │  ├─ header
│  │     │  │  ├─ _index.scss
│  │     │  │  ├─ _logo.scss
│  │     │  │  └─ _nav.scss
│  │     │  ├─ sidebar
│  │     │  │  ├─ _index.scss
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
├─ deploy
│  ├─ install.sh
│  ├─ systemd
│  │  ├─ webapp.service
│  │  └─ webhook.service
│  └─ webhook
│     ├─ webhook_listener.py
│     └─ webhook_requirements.txt
├─ deploy.sh
├─ doc
│  ├─ Behavioral Design
│  │  ├─ ActivityDiagram
│  │  ├─ ClassDiagram
│  │  ├─ ComponentDiagram
│  │  ├─ DeploymentDiagram
│  │  ├─ PackageDiagram
│  │  └─ SequenceDiagram
│  ├─ DataBase Desing
│  └─ High-Level Design
├─ docker-compose.yaml
├─ Dockerfile
├─ instance
│  └─ users.db
├─ migrations
│  ├─ alembic.ini
│  ├─ env.py
│  ├─ README
│  ├─ script.py.mako
│  └─ versions
│     ├─ a04c6e1155c3_initial_migration.py
│     └─ c7cb8d6f1375_add_role_column_to_user.py
├─ README.md
├─ requirements.txt
├─ run.py
└─ wsgi.py

```