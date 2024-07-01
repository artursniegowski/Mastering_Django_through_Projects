import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
# TODO: set to production settings, use this file in production!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.prod")

app = Celery("app")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
