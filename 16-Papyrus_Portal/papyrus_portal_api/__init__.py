from .celery import app as celery_app

# this is the code that will be executed when the
# celery worker is started. It will load the django settings
# module and then discover the tasks in the installed
# Django apps 
__all__ = ("celery_app",)  
