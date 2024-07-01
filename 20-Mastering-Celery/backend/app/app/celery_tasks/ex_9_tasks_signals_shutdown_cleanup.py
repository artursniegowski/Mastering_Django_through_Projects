# docker exec -it django-backend sh
# /app $ ./manage.py shell
# >>> from app.celery_tasks.ex_9_tasks_signals_shutdown_cleanup import run_task
# >>> run_task()
from celery.signals import task_failure
from app.celery import app
import sys


@app.task(queue='tasks')
def cleanup_failed_task(task_id, *args, **kwargs):
    sys.stdout.write("CLEAN UP")

@app.task(queue='tasks')
def my_task():
    raise ValueError("Number Error.")

# so whenever the my_task recive some kind of error, then this
# task_failure signal will be triggered
@task_failure.connect(sender=my_task)
def handle_task_failure(sender=None, task_id=None, **kwargs):
    cleanup_failed_task.delay(task_id)

def run_task():
    my_task.apply_async()
