import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.settings import Config  # Импортируем ваш config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Загружаем конфиг из класса Config

    db.init_app(app)  # Инициализация SQLAlchemy с приложением

    # Импорт моделей (обязательно после инициализации db)
    from app.models import users

    # Импорт маршрутов
    from app.routes import (
        main_routes,
        auth_routes,
        dashboard_routes,
        profile_routes,
        botmanager_routes,
    )

    # Регистрация blueprint'ов
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(dashboard_routes.bp)  # Раскомментируйте при необходимости
    app.register_blueprint(profile_routes.bp)
    app.register_blueprint(botmanager_routes.bp)

    return app
