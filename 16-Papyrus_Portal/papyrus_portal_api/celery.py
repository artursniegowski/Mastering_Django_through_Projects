import os

from celery import Celery
from django.conf import settings

# TODO: change this in production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "papyrus_portal_api.settings.local")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "papyrus_portal_api.settings.production")

# setting the name of the Celery instance, this name will be used to refer
# to this instance of celery in other parts of the system

app = Celery("papyrus_portal_api")  

# load the configuration from the Django settings module
# and the namespace argument is used to avoid
# clashes between the celery configuration and Django configuration
app.config_from_object("django.conf:settings", namespace="CELERY")

# the autodiscover taks is used to autmaticly discoer tasks in all
# the installed Django applications
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
