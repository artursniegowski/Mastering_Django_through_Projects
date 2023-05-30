"""
Django settings for littlelemon project.

Generated by 'django-admin startproject' using Django 4.2.
 
For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see 
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
  
from pathlib import Path
import os
########################################################################
# just for your local machine !! - to use vriables in the .env file
# you have to change the .env.example to .env and then define your MySQL password there
# NOT NEEDED IN PRODUCTION
from dotenv import load_dotenv
load_dotenv() 
########################################################################## 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

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
    # cusotm apps
    'restaurant.apps.RestaurantConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
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

ROOT_URLCONF = 'littlelemon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'littlelemon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

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
## TODO: dont forget to check your connection details such as : 'NAME', 'USER', 'PASSWORD', 'HOST', 'PORT'
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
#     }
# }
## <- ##

 
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ]
    # for rendering in json, html and xml
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        # 'rest_framework_xml.renderers.XMLRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        # if you want to use django admin login simoltenously with the browsable API
        # you need to add this sesion
        # TODO: comment out before submission
        # project will only suport token based authentication !
        'rest_framework.authentication.SessionAuthentication',
    ],
}

DJOSER = {
    # this is how you specify which field in your user model
    # will act as the primary key
    "USER_ID_FIELD":"username",
    # some peopel prefer to use the email addres as the username which you can change like so:
    # "LOGIN_FIELD":"email"
}
