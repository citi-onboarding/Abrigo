from .base import *


#Databases
# db_url = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
# default_db = dj_database_url.config(default=db_url, conn_max_age=500)
# DATABASES['default'].update(default_db)

SECURE_SSL_REDIRECT = True

SECURE_PROXY_SSL_HEADER = (‘HTTP_X_FORWARDED_PROTO’, ‘https’)

#Passwords

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

INSTALLED_APPS += []

MIDDLEWARE += []

