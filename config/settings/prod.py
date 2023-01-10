from .base import *

ALLOWED_HOSTS = ['13.124.212.248']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'PASSWORD': 'Fhwlr93!',
        'HOST': 'ls-ab4aa99fee1ed61217ace787743411ad809bff56.cy9bxtusp3br.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}