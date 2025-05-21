# base_config.py
import os
from dotenv import load_dotenv


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # База данных
    DB_PATH = os.path.join(BASE_DIR, 'instance', 'users.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f"sqlite:///{DB_PATH}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Загрузка файлов
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    UPLOAD_FOLDER = os.path.join('app', 'static', 'images', 'avatars')

    # API токен бота
    API_TOKEN = os.environ.get('API_TOKEN')

    # VPS
    VPS_IP = os.environ.get('VPS_IP')
    VPS_USER = os.environ.get('VPS_USER')
    VPS_PASSWORD = os.environ.get('VPS_PASSWORD')
