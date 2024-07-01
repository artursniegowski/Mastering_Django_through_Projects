import time

from celery import shared_task
from django.core.management import call_command

# calling the managment command with the help of celery
# so celery will call our custom created command
@shared_task
def management_command(queue="tasks"):
    call_command('test_command')


# sample tasks
@shared_task
def task1():
    return


@shared_task
def task2():
    return


# tasks for priority queue
# setting the task rate limit for a given task
@shared_task(task_rate_limit="1/m")
def tp1(queue="celery"):
    time.sleep(3)
    return


@shared_task
def tp2(queue="celery:1"):
    time.sleep(3)
    return


@shared_task
def tp3(queue="celery:2"):
    time.sleep(3)
    return


@shared_task
def tp4(queue="celery:3"):
    time.sleep(3)
    return


