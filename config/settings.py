# settings.py

import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.environ.get('FLASK_ENV', 'development')

if ENV == 'production':
    from .prod_config import ProductionConfig as Config
else:
    from .dev_config import DevelopmentConfig as Config
