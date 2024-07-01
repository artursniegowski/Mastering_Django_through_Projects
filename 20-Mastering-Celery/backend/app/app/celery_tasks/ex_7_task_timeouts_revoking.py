# docker exec -it django-backend sh
# /app $ ./manage.py shell
# >>> from app.celery_tasks.ex_7_task_timeouts_revoking import long_runnig_task, execute_task_examples
# >>> long_runnig_task.delay()
from app.celery import app
from time import sleep
import sys

# time limit is set in seconds so hre we have 5 seconds
# time limit excedded exception if the task will be over that time
@app.task(queue='tasks', time_limit=10)
def long_runnig_task():
    sleep(6)
    return "Task completed successfully"


@app.task(queue='tasks', bind=True)
def process_task_result(self, result):
    if result is None:
        return "Task was revoked, skipping result processing"
    else:
        return f"Task results: {result}"

def execute_task_examples():
    result = long_runnig_task.delay()
    try:
        # we specifying that we want to wait up to 4 seconds for the result
        task_result = result.get(timeout=20)
    except TimeoutError as e:
        print("Task timed out.")
        
    task = long_runnig_task.delay()
    task.revoke(terminate=True)
    # this will be pending
    sys.stdout.write(task.status)
    sleep(3)
    # this will be revoke
    sys.stdout.write(task.status)
    
    if task.status == 'REVOKED':
        process_task_result.delay(None) # task was revoked
    else:
        process_task_result.delay(task.result)
    
    

