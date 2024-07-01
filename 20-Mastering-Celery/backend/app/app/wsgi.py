"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# TODO: default set to development settings, replace the whole file for production!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.dev")

application = get_wsgi_application()
