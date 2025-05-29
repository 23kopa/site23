from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_migrate import Migrate

from config.settings import Config


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate() 


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Загружаем конфиг из класса Config

    db.init_app(app)  # Инициализация SQLAlchemy с приложением
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth_routes.login'

    from app.models.users import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Импорт маршрутов
    from app.routes.index_routes import (
        main_routes,
        auth_routes
    )

    from app.routes.pages_routes import (
        profile_routes,
        botmanager_routes,
        dashboard_routes
    )

    # Регистрация blueprint'ов
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(profile_routes.bp)
    app.register_blueprint(botmanager_routes.bp)
    app.register_blueprint(dashboard_routes.bp)

    EXEMPT_PATHS = [
        '/',
        '/login',
        '/register',
        '/static/',
        '/welcome',
    ]

    @app.before_request
    def require_login():
        if not current_user.is_authenticated:
            path = request.path
            # Если путь не начинается с одного из исключений — редиректим на логин
            if not any(path.startswith(exempt) for exempt in EXEMPT_PATHS):
                return redirect(url_for('auth_routes.login'))

    return app
