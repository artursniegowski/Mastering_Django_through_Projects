# docker exec -it django-backend sh
# /app $ ./manage.py shell
# >>> from app.celery_tasks.ex_13_task_schedule_crontrab import task1, task2
# >>>
"""
* * * * *
| | | | |
| | | | +------ Day of the Week (0-6) (Sunday = 0 or 7)
| | | +-------- Month (1-12)
| | +---------- Day of the Month (1-31)
| +------------ Hour (0-23)
+-------------- Minute(0-59)
"""
# some examples
"""
* * * * *          # Run every minute
*/5 * * * *        # Run every 5 minuts
30 * * * *         # Run every hour at 30 minutes past the hour
0 9 * * *          # Run every dayat 9AM
0 14 * * 1         # Run every Monday at 2PM
0 20,23 * * 5      # Run every Friday at 8 PM and 11PM
0 0-8/2 * * *      # Run every 2 hours from midnight to 8 AM
0 0 1 1 MON        # Run on thefirst Monday of January every year
"""

from datetime import timedelta
from app.celery import app
from celery.schedules import crontab

# TODO: uncomment for running the task in scheduled time
# app.conf.beat_schedule = {
#     'task1':{
#         'task': 'app.celery_tasks.ex_13_task_schedule_crontrab.task1',
#         # This is teh default * * * * *, which will run every minute
#         'schedule': crontab(),
#         'kwargs': {'foo':'bar'},
#         'args': (1,2),
#         'options': {
#             'queue':'tasks',
#             'priority': 5,    
#         },
#     },
#     'task2':{
#         'task': 'app.celery_tasks.ex_13_task_schedule_crontrab.task2',
#         # schedule the task every 2 minutes
#         # 'schedule': crontab(minute='*/2'),
#         # minute='0-59/10': This means the task will run every 10 minutes within each hour. The 0-59/10 syntax specifies a range from 0 to 59 with a step of 10.
#         # hour='0-5': This specifies that the task will only run between midnight (00:00) and 5 AM (05:00).
#         # day_of_week='mon': This specifies that the task will only run on Mondays.
#         'schedule': crontab(minute='0-59/10', hour='0-5', day_of_week='mon'),
#     }
# }

@app.task(queue='tasks')
def task1(a, b, **kwargs):
    res = a + b
    print(f"Running task 1: {res}")

@app.task(queue='tasks')
def task2():
    print("Running task 2")