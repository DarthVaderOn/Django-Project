from time import sleep
from celery import shared_task


@shared_task
def send_email_task():
    sleep(10)

    return None