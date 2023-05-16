"""
Django settings for sqlalchemy_test project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import sqlalchemy 
from sqlalchemy.orm import scoped_session, sessionmaker
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
    # these apps will add tables to the database; 
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # custom apps
    'app_add_models',
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

ROOT_URLCONF = 'sqlalchemy_test.urls'

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

WSGI_APPLICATION = 'sqlalchemy_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# connection fro sqlalchemy
MYSQL_URI = f"mysql+pymysql://{os.environ.get('MYSQL_USER', 'root')}:{os.environ.get('MYSQL_PASSWORD')}@{os.environ.get('MYSQL_DATABASE_HOST', '127.0.0.1')}:{os.environ.get('MYSQL_DATABASE_PORT', '3306')}/{os.environ.get('MYSQL_DATABASE_NAME')}"

DATABASES = {
    'default': {
        'NAME':os.environ.get('MYSQL_DATABASE_NAME'),
        'USER':os.environ.get('MYSQL_USER','root'),
        'PASSWORD':os.environ.get('MYSQL_PASSWORD'),
        'HOST':os.environ.get('MYSQL_DATABASE_HOST','127.0.0.1'),
        'PORT':os.environ.get('MYSQL_DATABASE_PORT', '3306'),
        'OPTIONS': { 
            'charset': 'utf8mb4', # for more charactersets like emojis
        },
        # django requires the engine to be defined , so i migth as well use the engine 
        'ENGINE': 'django.db.backends.mysql',
        'SA_ENGINE': sqlalchemy.create_engine(
            MYSQL_URI, pool_recycle=3600, pool_size=10, max_overflow=20
        ),
    }
}

## session for sqlalchemy
SA_DB_SESSION=scoped_session(sessionmaker(bind=DATABASES['default']['SA_ENGINE'], autocommit=False, autoflush=False))
# db_session = SA_DB_SESSION()

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
