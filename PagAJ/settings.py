"""
Django settings for PagAJ project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import django_heroku
import os

#import dj_database_url
from decouple import config


from pathlib import Path
from django.core.mail import send_mail

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_PRO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '001482f592662766200d43c46f990d77671f84d9cbdcecd1'
SECRET_KEY = os.environ.get('SECRET_KEY_DJANGO')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://aj-ra-l.herokuapp.com/']

# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'AJ/static'),
#    ]



# Application definition

INSTALLED_APPS = [
    'AJ',
    'Contacto.apps.ContactoConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PagAJ.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '~/PagAJ/AJ/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PagAJ.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Para PostgreSQL 
# DATABASES = {
#     'default': {
#         # BB.DD de Contacto de Clientes
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'Contacto_Clientes',
#         'USER': 'postgres',
#         'PASSWORD': os.environ.get('PASSWORD_DB'),
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }
# # Para usar varias BB.DD
# Mas informacion en: https://docs.djangoproject.com/en/2.1/topics/db/multi-db/#automatic-database-routing

# DATABASES = {
#     'default': {
#         'NAME': 'PagAJ',
#         'ENGINE': 'django.db.backends.postgresql',
#         'USER': 'postgres',
#         'PASSWORD': os.environ.get('PASSWORD_DB'),
#         'HOST': '127.0.0.1',
#         'PORT': '5432'
#     },
#     'bd_contacto': {
#         'NAME': 'Contacto_Clientes',
#         'ENGINE': 'django.db.backends.postgresql',
#         'USER': 'postgres',
#         'PASSWORD': os.environ.get('PASSWORD_DB'),
#         'HOST': '127.0.0.1',
#         'PORT': '5432'
#     }
# }

# add this

#db_from_env = dj_database_url.config()
#DATABASES['default'].update(db_from_env)
#DATABASES['default']['CONN_MAX_AGE'] = 500


DATABASE_ROUTERS = ['Contacto.router.Contacto_Router','AJ.router.AJ_Router']

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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




# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Envio de Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'  
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
EMAIL_PORT=587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER_EMAIL')  
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD_EMAIL') 
DEFAULT_EMAIL_FROM = os.environ.get('EMAIL_HOST_USER_EMAIL')
EMAIL_HOST_RECIPIENT=os.environ.get('EMAIL_RECIPIENT_LIST')

django_heroku.settings(locals())

