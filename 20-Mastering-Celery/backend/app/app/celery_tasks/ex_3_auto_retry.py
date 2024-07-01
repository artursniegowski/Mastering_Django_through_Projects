from app.celery import app
from celery import Task
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

class CustomTask(Task):
    # method handling task failure
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error('Connection error occured - custom task!')
        else:
            print("{0!r} failed: {1!r}".format(task_id, exc))

# using the customtask as my task
app.Task = CustomTask

# so autoretry if the ConnectionError occures
# setting the default_retry_delay to 5 seconds - we will retry the task every 5 seconds
# max number of retries = 3
@app.task(queue='tasks', autoretry_for=(ConnectionError,), default_retry_delay=5, retry_kwargs={'max_retries':3})
def my_task():
    raise ConnectionError("Conection error occured here and now.")
    return
