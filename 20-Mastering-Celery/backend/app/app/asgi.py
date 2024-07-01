"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# TODO: default set to development settings, replace the whole file for production!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.dev")

application = get_asgi_application()
