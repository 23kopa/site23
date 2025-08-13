from flask_wtf import CSRFProtect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config.settings import Config

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    login_manager.login_view = 'auth.login'

    from app.models.users import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Импорт маршрутов
    from app.routes.frontend import (
        home_routes,
        tokensboard_routes
    )

    from app.routes.api.token.web import (
        creation_web,
        trigger_web
    )

    # Регистрация blueprint'ов
    app.register_blueprint(tokensboard_routes.bp)
    app.register_blueprint(home_routes.bp)

    app.register_blueprint(creation_web.bp, url_prefix='/token_generate')
    app.register_blueprint(trigger_web.bp, url_prefix='/token')

    return app
