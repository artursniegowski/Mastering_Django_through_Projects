import logging

from celery import Task

from app.celery import app

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
)


class CustomTask(Task):
    # method handling task failure
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        if isinstance(exc, ConnectionError):
            logging.error("Connection error occured - custom task!")
        else:
            print("{0!r} failed: {1!r}".format(task_id, exc))


# using the customtask as my task
app.Task = CustomTask


@app.task(queue="tasks")
def my_task():
    try:
        raise ConnectionError("Connection Error Occured...")
    except ConnectionError as e:
        raise ConnectionError()
    except ValueError as e:
        logging.error("Value error occured.")
        raise ValueError()
