# docker exec -it django-backend sh
# /app $ ./manage.py shell
# >>> from app.celery_tasks.ex_12_task_scheduling_customization import task1, task2
# >>>
from datetime import timedelta
from app.celery import app

# TODO: uncomment for running the task in intervals
# app.conf.beat_schedule = {
#     'task1':{
#         'task': 'app.celery_tasks.ex_12_task_scheduling_customization.task1',
#         # schedule the task every 10 seconds
#         'schedule': timedelta(seconds=10),
#         'kwargs': {'foo':'bar'},
#         'args': (1,2),
#         'options': {
#             'queue':'tasks',
#             'priority': 5,    
#         },
#     },
#     'task2':{
#         'task': 'app.celery_tasks.ex_12_task_scheduling_customization.task2',
#         # schedule the task every 15 seconds
#         'schedule': timedelta(seconds=15),
#     }
# }

@app.task(queue='tasks')
def task1(a, b, **kwargs):
    res = a + b
    print(f"Running task 1: {res}")

@app.task(queue='tasks')
def task2():
    print("Running task 2")