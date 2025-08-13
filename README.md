
```
botmanager
├─ .dockerignore
├─ app
│  ├─ extensions
│  │  └─ redis.py
│  ├─ models
│  │  ├─ reminders.py
│  │  ├─ tokens.py
│  │  ├─ users.py
│  │  └─ __init__.py
│  ├─ routes
│  │  ├─ api
│  │  │  └─ token
│  │  │     ├─ dns
│  │  │     ├─ excel
│  │  │     ├─ image
│  │  │     ├─ qr
│  │  │     │  ├─ creation_qr.py
│  │  │     │  └─ trigger_qr.py
│  │  │     ├─ web
│  │  │     │  ├─ creation_web.py
│  │  │     │  └─ trigger_web.py
│  │  │     └─ word
│  │  └─ frontend
│  │     ├─ home_routes.py
│  │     └─ tokensboard_routes.py
│  ├─ services
│  │  ├─ content
│  │  │  ├─ components
│  │  │  │  ├─ cards
│  │  │  │  │  └─ tokens_cards.py
│  │  │  │  └─ modals
│  │  │  │     └─ tokens_modals.py
│  │  │  └─ pages
│  │  │     ├─ home_content.py
│  │  │     └─ tokens_content.py
│  │  ├─ kv
│  │  │  └─ redis_store.py
│  │  ├─ token_engines
│  │  │  ├─ base_token.py
│  │  │  ├─ dns_token.py
│  │  │  ├─ excel_token.py
│  │  │  ├─ image_token.py
│  │  │  ├─ qr_token.py
│  │  │  ├─ web_token.py
│  │  │  ├─ word_token.py
│  │  │  └─ __init__.py
│  │  └─ vps
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
│  │  │  ├─ gif
│  │  │  │  ├─ homegif.gif
│  │  │  │  └─ spbgut.gif
│  │  │  ├─ icons
│  │  │  └─ logo.png
│  │  ├─ js
│  │  │  ├─ cpu.js
│  │  │  ├─ disk.js
│  │  │  ├─ main.js
│  │  │  ├─ matrix.js
│  │  │  ├─ network.js
│  │  │  ├─ nginx.js
│  │  │  ├─ script.js
│  │  │  └─ showToken.js
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
│  │     │  │  └─ _btn-card.scss
│  │     │  ├─ cards
│  │     │  │  ├─ card_class
│  │     │  │  │  └─ _card-token.scss
│  │     │  │  └─ card_type
│  │     │  │     └─ _card-small.scss
│  │     │  ├─ forms
│  │     │  │  └─ _form-base.scss
│  │     │  ├─ items
│  │     │  │  ├─ _bg-dark.scss
│  │     │  │  ├─ _features.scss
│  │     │  │  ├─ _header.scss
│  │     │  │  ├─ _scrollbar.scss
│  │     │  │  └─ _tokens_table.scss
│  │     │  ├─ modals
│  │     │  │  └─ modal-base
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
│  │     │  ├─ _default_original.scss
│  │     │  └─ _index.scss
│  │     └─ vendors
│  │        ├─ _bootstrap.scss
│  │        └─ _index.scss
│  ├─ templates
│  │  ├─ base
│  │  │  ├─ base.html
│  │  │  ├─ navbar.html
│  │  │  ├─ trigger_gif.html
│  │  │  └─ welcome.html
│  │  ├─ components
│  │  │  ├─ cards
│  │  │  │  ├─ action_card.html
│  │  │  │  └─ static_card.html
│  │  │  └─ modals
│  │  │     ├─ token_generate_modal.html
│  │  │     ├─ token_result_modal.html
│  │  │     └─ token_select_moda.html
│  │  ├─ macros
│  │  │  └─ __init__.html
│  │  └─ pages
│  │     ├─ home.html
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
│     ├─ 19b41ba38d48_add_email_and_alert_message_columns_to_.py
│     ├─ 7fd4eea37f58_add_tokens_table.py
│     ├─ a04c6e1155c3_initial_migration.py
│     └─ c7cb8d6f1375_add_role_column_to_user.py
├─ README.md
├─ requirements.txt
├─ run.py
└─ wsgi.py

```