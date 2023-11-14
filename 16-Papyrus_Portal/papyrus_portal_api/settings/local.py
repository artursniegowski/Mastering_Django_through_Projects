from .base import *  # noqa
from .base import env

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
# SECRET_KEY = env('SECRET_KEY')
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="7rTclLWo9GI9RqcR8LCCvA7eFHcB142N9fW-ealb3Ti5KX-fieY",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# CSRF_TRUSTED_ORIGINS
# https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-trusted-origins
CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

# configure the celery email backend
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@noreplay.site"
DOMAIN = env("DOMAIN")
SITE_NAME = "Papyrus Portal"
