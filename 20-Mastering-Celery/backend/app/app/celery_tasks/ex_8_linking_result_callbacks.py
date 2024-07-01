# docker exec -it django-backend sh
# /app $ ./manage.py shell
# >>> from app.celery_tasks.ex_8_linking_result_callbacks import run_task
# >>> run_task()
from app.celery import app
import sys


@app.task(queue='tasks')
def long_runnig_task():
    raise ValueError("Numbers are not correct.")

@app.task(queue='tasks')
def process_task_result(result):
    sys.stdout.write("Process task results")
    sys.stdout.flush()
    
@app.task(queue='tasks')
def error_handles(task_id, exc, traceback):
    sys.stdout.write("########################")
    sys.stdout.write(str(exc))
    sys.stdout.write("########################")
    sys.stdout.flush()

def run_task():
    # linking tasks with link
    # link_error is called when link process fails or the first task fails.
    long_runnig_task.apply_async(link=[process_task_result.s(),], link_error=[error_handles.s(),])
    
    

