# from snd.snd.settings import INSTALLED_APPS
# from snd.snd.settings import DEBUG
from .base import *

# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

EMAIL_BACKEND ='django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS += [
    # 'debug_toolbar',
]