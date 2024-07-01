# docker exec -it django-backend sh
# /app $ ./manage.py shell
# >>> from app.celery_tasks.ex_6_dead_letter_queue import run_task_group
# >>> run_task_group()
from app.celery import app
from celery import group

# enables late acknowledgement of tasks in celery
# tasks are not ack immediately after they are received from the worker
# instead teh ack is sent adter the task has been executed
app.conf.task_acks_late = True
# determines teh behavior of the worker when it is lost or disconnected
# from the message broker
app.conf.task_reject_on_worker_lost = True


@app.task(queue='tasks')
def my_task(z):
    try:
        if z==2:
            raise ValueError("Error wrong number.")
    except ValueError as e:
        # so itis going to move teh task to a new queue
        # this will happen when the task fails
        handle_failed_task.apply_async(args=(z,str(e)))
        raise ValueError


@app.task(queue='dead_letter')
def handle_failed_task(z, exception):
    return "Custom logic to process the failed task."


def run_task_group():
    task_group = group(
        my_task.s(1),
        my_task.s(2),
        my_task.s(3),
    )
    task_group.apply_async()
