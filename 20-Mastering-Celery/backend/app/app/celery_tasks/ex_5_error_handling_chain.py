# >>> from app.celery_tasks.ex_5_error_handling_chain import run_task_chain
# >>> run_task_chain()
from app.celery import app
from celery import chain

## when the error occures in the multiple task
# then the chain will stop there and not continue handlign next tasks

@app.task(queue='tasks')
def add(x, y):
    return x + y

@app.task(queue='tasks')
def multiply(z):
    if z == 5:
        raise ValueError("Error: Division by Zero")
    return z*2


def run_task_chain():
    task_chain = chain(add.s(2,3), multiply.s())
    result = task_chain.apply_async()
    result.get()