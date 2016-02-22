from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'traveleando',
        'USER': perfil['databases']['user'],
        'PASSWORD': perfil['databases']['password'],
        'HOST': 'localhost',
        'PORT': ''
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), 'static'),
)

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
MEDIA_URL = '/'