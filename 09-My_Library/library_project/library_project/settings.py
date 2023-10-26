"""
Django settings for library_project project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path 
 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# retrived from the docker-composer ENV variables
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG is 1 = True, and if DEBUG is 0 = False (or not defined, or any other)
# retrived from the docker-composer ENV variables
DEBUG = bool(os.environ.get('DEBUG', 0)=='1') 

# accessible only via specific host name
# so you want to make sure only that hostname can be used because otherwise
# it can open your applciation fro certain vulnerabilities
# we will accept a coma seperated list and we will add all of them
# bc there can be many
ALLOWED_HOSTS = []
# so we are getting all the hosts, and if it dosent exists we will set an emty value ''
# next we are spliting everything by a coma, so many hosts can be defined with a coma,
# and filter out all the None vals,
# so basicaly if the list is empty the filter function will return empty list
# and extedn will not add anything to the empty list, otherwise we add all the hosts
ALLOWED_HOSTS.extend(
    filter(
        None,
        # retrived from the docker-composer ENV variables
        os.environ.get('ALLOWED_HOSTS', '').split(','),
    )
)


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
    'app_catalog.apps.AppCatalogConfig',
    'app_core.apps.AppCoreConfig',
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

ROOT_URLCONF = 'library_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'library_project.context_processors.get_current_year_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'library_project.wsgi.application'


# Database - PostgreSQL
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# retrived from the docker-composer ENV variables
# DB_HOST  
# DB_NAME 
# DB_USER 
# DB_PASS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # these settings are retrived from the docker-composer ENV variables
        'HOST': os.environ.get('DB_HOST'), 
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        # not specifying the port number -> Django will use the default 
        # port number for PostgreSQL databse which is 5432
        # 'PORT': os.environ.get('DATABASE_PORT'),
    }
}


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

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/static/'
MEDIA_URL = 'static/media/'

# additonal dirs to look for static files
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# $ python manage.py collectstatic
# This will copy all files from your static folders into the STATIC_ROOT 
# directory.

STATIC_ROOT = '/vol/web/static'
MEDIA_ROOT = '/vol/web/media'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

# TODO: For testing
# This logs any emails sent to the console - for testing
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
