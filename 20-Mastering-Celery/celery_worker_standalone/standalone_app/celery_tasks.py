import os
from datetime import timedelta
from celery import Celery
from sentry_sdk import init
from sentry_sdk.integrations.celery import CeleryIntegration

## sentry configuration - START ##
SENTRY_SDK_DSN = os.environ.get('SENTRY_SDK_DSN')

init(dsn=SENTRY_SDK_DSN, integrations=[CeleryIntegration()])
## sentry configuration - END ##

app = Celery('standalone-celery-app')

app.config_from_object("celeryconfig", namespace="CELERY")
app.conf.imports = ('celery_app.tasks',)

# this might not be neededif import is included as above
app.autodiscover_tasks()

### adding scheduler - START ###
app.conf.beat_schedule = {
    'task1':{
        # this task will check if the website is up
        'task': 'celery_app.tasks.check_webpage',
        # schedule the task every 30 seconds
        'schedule': timedelta(seconds=30),
    },
}
### adding scheduler - END ###