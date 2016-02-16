from base import *

DEBUG = True
database = credentials['database']['local']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME' : 'project',
		'USER': database['user'],
		'PASSWORD': database['password'],
		'HOST': 'localhost',
		'PORT': ''
	}
}

STATIC_URL = '/static/'