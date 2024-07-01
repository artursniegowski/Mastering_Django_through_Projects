from celery import shared_task
import requests
# this way we can tell sentry to just capture an error
from sentry_sdk import capture_exception

# just an examplpe
@shared_task
def task2():
    return

# checking if webpage is up
@shared_task
def check_webpage():
    try:
        # refering to the nginx service running that is the proxy for my django backend
        # default port is the port 80
        # resp = requests.get('http://127.0.0.1:8000')
        headers = {
            'Host': 'localhost'
        }
        resp = requests.get("http://nginx/admin", headers=headers)
        # print("######################")
        # print(resp.status_code)
        # print("######################")
        if resp.status_code != 200:
            raise Exception(f"Website is down. Check it now!")
    except requests.exceptions.RequestException as e:
        # we sending this exception manually back to sentry as sentry woudl not pick
        # up the exception from above
        capture_exception(e)