# docker exec -it django-backend sh
# /app $ ./manage.py shell
# >>> from app.celery_tasks.ex_10_error_tracking_monitoring_Sentry import divide_numbers
# >>> divide_numbers.delay(10,0)
# setting manually when we want to capture an exception
from sentry_sdk import capture_exception
from app.celery import app
import sys

@app.task(queue='tasks')
def divide_numbers(a, b):
    try:
        result = a/b
        return result
    except ZeroDivisionError as e:
        raise e
