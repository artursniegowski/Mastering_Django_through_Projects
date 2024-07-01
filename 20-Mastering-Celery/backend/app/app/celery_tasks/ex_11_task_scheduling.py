# docker exec -it django-backend sh
# /app $ ./manage.py shell
# >>> from app.celery_tasks.ex_11_task_scheduling import task1, task2
# >>>
from datetime import timedelta
from app.celery import app

# TODO: uncomment for running the task in intervals
# app.conf.beat_schedule = {
#     'task1':{
#         'task': 'app.celery_tasks.ex_11_task_scheduling.task1',
#         # schedule the task every 10 seconds
#         'schedule': timedelta(seconds=10),
#     },
#     'task2':{
#         'task': 'app.celery_tasks.ex_11_task_scheduling.task2',
#         # schedule the task every 15 seconds
#         'schedule': timedelta(seconds=15),
#     }
# }

@app.task(queue='tasks')
def task1():
    print("Running task 1")

@app.task(queue='tasks')
def task2():
    print("Running task 2")