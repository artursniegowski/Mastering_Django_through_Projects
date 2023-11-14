from .base import *  # noqa
from .base import env

# ADMINS
# A list of all the people who get code error notifications.
# When DEBUG=False and AdminEmailHandler is configured in LOGGING
# (done by default), Django emails these people the details of
# exceptions raised in the request/response cycle.
# https://docs.djangoproject.com/en/4.2/ref/settings/#admins
ADMINS = [
    ("Bob Tester", "bobtester@noreplay.com"),
]

# add domain names of the porduction server
# CSRF_TRUSTED_ORIGINS
## list of domains that are allowed to make cross-sire requests
# https://docs.djangoproject.com/en/4.2/ref/settings/#csrf-trusted-origins
CSRF_TRUSTED_ORIGINS = ["https://yourdomainname.com"]

# SECURITY WARNING: keep the secret key used in production secret!
# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
# SECRET_KEY = env('SECRET_KEY')
SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["https://yourdomainname.com"])

ADMIN_URL = env("DJANGO_ADMIN_URL")

DATABASES = {"default": env.db("DATABASE_URL")}

# it is a tuple of strigs that represents the header and value that indicates a request 
# is secure, this is used by the security middleware to determine if a request 
# is secure
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

# determins if the session cookies should be set with the secure flag
SESSION_COOKIE_SECURE = True

# determines if the csrf cookie shoudl be sent with a secure flag
CSRF_COOKIE_SECURE = True

# HTTP strict transport security, it is a security policy that lets our server enforce 
# that web browsers shoudl only interact via HTTPS by adding a strict transport
# security header, 6 days = 518400 sec
# TODO change to 518400 later, first 60 for testing
SECURE_HSTS_SECONDS = 60

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)

# it determinates if the x contetn type options header should be set to no sniff,
# which prevents the browser from guessing the contetn type and force it to always use
# the type provided in the contetnt type header
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

# using whitenoise fro static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="Papyrus Portal Support <support@trainingwebdev.com>",
)

SITE_NAME = "Papyrus Portal"

# the actual email addres teh email will be sent from
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)

EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="[Papyrus Portal]",
)

# mailgun configurations
# configure the celery email backend
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = "smtp.mailgun.org"
EMAIL_HOST_USER = "postmaster@mg.yourdomainname.com"
EMAIL_HOST_PASSWORD = env("SMTP_MAILGUN_PASSWORD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DOMAIN = env("DOMAIN")

# configuring login
# Loggers
# https://docs.djangoproject.com/en/4.2/topics/logging/#logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        # mail admin, handler that emails the admins with the details of the exception
        # raised in the request response cycle, This is only used if the debug setting
        # is flase, so for Production
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console"],
    },
    "loggers": {
        # logs the request, response cycle, only used when DEBUG = FALSE => in porduction
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        # disallowedhost is a logger that logs when a request is made to a host that
        # is not the allowed host settings, this can only be used when DEBUG = FALSE => PRODUCTION
        "django.security.DisallowedHost": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}