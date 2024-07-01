import os
import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from celery import Celery
from kombu import Exchange, Queue

# import time


# set the default Django settings module for the 'celery' program.
# TODO: default set to development settings, replace the whole file for production!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.dev")

app = Celery("app")

######## SETTING UP SENTRY - START #######
# https://docs.sentry.io/platforms/python/integrations/django/

SENTRY_SDK_DSN = os.environ.get('SENTRY_SDK_DSN')

sentry_sdk.init(
    dsn=SENTRY_SDK_DSN,
    integrations=[CeleryIntegration()]
)

######## SETTING UP SENTRY - END #######

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

## SETTINGS FOR RABBITMQ  - START ##
app.conf.task_queues = [
    Queue(
        "tasks",
        Exchange("tasks"),
        routing_key="tasks",
        # 10 is the highest priority and 1 the lowest
        queue_arguments={"x-max-priority": 10},
    ),
    # adding a dead letter queue where messages that cannot be processed successfully 
    # by workers are sent for further inspection or reprocessing
    # celery will use the default exchange which is a direct exchange with the same name
    # as the queue
    Queue(
        "dead_letter", routing_key="dead_letter",
    ),
]


# enables late acknowledgement of tasks in celery
# tasks are not ack immediately after they are received from the worker
# instead teh ack is sent adter the task has been executed
app.conf.task_acks_late = True

app.conf.task_default_priority = 5
# prefetch is a mechanism that allows the worker to fetch multiple tasks
# from the broker at once, which can improve performance by reducing network and overheads
app.conf.worker_prefetch_multiplier = 1
# number of worker processes or threads that celery will spawn to process tasks concurently
# so this will lead to processing tasks sequentialy
app.conf.worker_concurrency = 1


# Load task modules from all registered Django apps.
# autodiscovering tasks in the new folder
# adding the autodiscover of the celery_tasks folder
# and checkign for all file that begin with ex to check for tasks in it
base_dir = os.getcwd()
task_folder = os.path.join(base_dir, "app", "celery_tasks")
if os.path.exists(task_folder) and os.path.isdir(task_folder):
    # finding all the files beging with ex
    # looking for all the tasks in thoes files
    task_modules = []
    for filename in os.listdir(task_folder):
        if filename.startswith("ex") and filename.endswith(".py"):
            # without the extension
            module_name = f"app.celery_tasks.{filename[:-3]}"
            # dynamically importing the module, this way we will have access
            # to all the data from the file
            module = __import__(module_name, fromlist=["*"])
            for name in dir(module):
                obj = getattr(module, name)
                if callable(obj) and name.startswith("my_tasks"):
                    task_modules.append(f"{module_name}.{name}")

    app.autodiscover_tasks(task_modules)
    
# this way we also autodiscover task from other apps that are in a tasks.py file
# not neceserly needed
# app.autodiscover_tasks()


## example tasks for the rabitmq to show how to change their priority


## also passing arguments, returning results example
# @app.task(queue="tasks")
# def t1(a, b, message=None):
#     time.sleep(3)
#     result = a + b
#     if message:
#         result = f"{message}: {result}"
#     return result


# @app.task(queue="tasks")
# def t2():
#     time.sleep(3)
#     return


# @app.task(queue="tasks")
# def t3():
#     time.sleep(3)
#     return


# ## SETTINGS FOR RABBITMQ  - END ##

# ## SETTINGS FOR REDIS - START ##
# # assiging different routes for different tasks
# # app.conf.task_routes = {
# #     "celery_app.tasks.task1": {"queue": "queue1"},
# #     "celery_app.tasks.task2": {"queue": "queue2"},
# # }

# # configuring task rate limiting
# # we setting it for 1 per minute
# # we can also set this in teh task decorator
# # shared_task(task_rate_limit='1/m')
# # app.conf.task_default_rate_limit = '1/m'

# # creating priorty queues
# # app.conf.broker_transport_options = {
# #     # consolidated into 4 levels - we created 4 queues
# #     # which are: celery, celery:1, celery:2, celery:3
# #     "priority_steps": list(range(10)),
# #     "sep": ":",
# #     "queue_order_strategy": "priority",
# # }

# ## SETTINGS FOR REDIS - END ##


# # Load task modules from all registered Django apps.
# app.autodiscover_tasks()


# ## testing functions for AsyncResult
# def test():
#     # call the task asynchrnously
#     res = t1.apply_async(args=[5, 10], kwargs={"message": "The sum is"})

#     # Check if the task has completed
#     if res.ready():
#         print("Task has completed")
#     else:
#         print("Task is still running")

#     # Check if the task completed successfully
#     if res.successful():
#         print("Task completed successfully")
#     else:
#         print("Task encountered an error")

#     # get the result of the task
#     try:
#         task_res = res.get()
#         print("Task result:", task_res)
#     except Exception as e:
#         print("An exception occurred:", str(e))

#     # Get the exception (if any) that occured during task execution
#     exc = res.get(propagate=False)
#     if exc:
#         print("An exception occured during task execution:", str(exc))


# # example for synchronous task execution
# def execute_sync():
#     res = t1.apply_async(args=[5, 10], kwargs={"message": "The sum is"})
#     task_res = res.get()
#     print("Task is running synchronously")
#     print(task_res)


# # example for asynchronous task execution
# def execute_async():
#     res = t1.apply_async(args=[5, 10], kwargs={"message": "The sum is"})
#     print("Task is running asynchronously")
#     print("Task ID:", res.task_id)
