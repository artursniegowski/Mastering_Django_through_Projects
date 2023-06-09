"""
Django settings for Restaurant project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
########################################################################
# just for your local machine !! - to use vriables in the .env file
# NOT NEEDED IN PRODUCTION
from dotenv import load_dotenv
load_dotenv()
##########################################################################


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# TODO: DJANGO_SECRET_KEY needs to be defined as env variable !
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# TODO: change to False for production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # custom apps
    'RestaurantManagementAPI.apps.RestaurantmanagementapiConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Restaurant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Restaurant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# configurations for sqlite database
# uncomment this:
## -> ##
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
## <- ##

## configurations for MySQL database
## uncomment this:
## -> ##
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME':'mydatabase',
#         'USER':'root',
#         'PASSWORD':os.environ.get('MYSQL_PASSWORD'),
#         'HOST':'127.0.0.1',
#         'PORT': '3306',
#         'OPTIONS': {   
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",   
#         },  
#     }
# }
## <- ##

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# additional settings for rest_framework
REST_FRAMEWORK = {
    # for rendering in json, html and xml
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        # 'rest_framework_xml.renderers.XMLRenderer',
    ],
    # for token based authentication as base auth metod
    # and then you will have to add to a api request also a token like so:
    # in auth choose the Bearer Token
    # token : paste your token
    # prefix: Token
    # this will sent the authentication token as:
    # Authorization: Token jdal33h42j5v1g52jg5v45jv125jg52
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        # if you want to use django admin login simoltenously with the browsable API
        # you need to add this sesion
        # TODO: comment out before submission
        # project will only suport token based authentication !
        'rest_framework.authentication.SessionAuthentication',
    ],
    # throttle policies !
    # for class based views
    # limiting the amount of request users can make to 50 per minute
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '50/minute',
        'user': '50/minute',

    },
    # DRFs build in pagination
    # commented out the pagination as global setting, 
    # bc pagination only enable for three endpoints
    # /api/menu-items
    # /api/orders    
    # /api/categories
    # this is why in the views for these two endpoints there is a atribute added for pagination
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # here we only are setting the page size for the pagination
    # 'PAGE_SIZE': 2,
    # since we use the custom paginator we don need global settings for it !!
}

DJOSER = {
    # this is how you specify which field in your user model
    # will act as the primary key
    "USER_ID_FIELD":"username",
    # some peopel prefer to use the email addres as the username which you can change like so:
    # "LOGIN_FIELD":"email"
}