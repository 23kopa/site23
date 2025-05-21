# prod_config.py

from .base_config import BaseConfig

class ProductionConfig(BaseConfig):
    DEBUG = False
    ssl_context=('/etc/letsencrypt/live/botmanager.site/fullchain.pem', '/etc/letsencrypt/live/botmanager.site/privkey.pem')