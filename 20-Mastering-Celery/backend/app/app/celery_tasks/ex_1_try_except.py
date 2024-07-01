import logging

from app.celery import app

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(message)s",
)


@app.task(queue="tasks")
def my_task():
    try:
        raise ConnectionError("Connection Error Occured...")
    except ConnectionError as e:
        logging.error("Connection error occured!")
        raise ConnectionError()
    except ValueError as e:
        logging.error("Value error occured.")
        raise ValueError()


# @app.task(queue='tasks')
# def my_task_2():
#     pass
