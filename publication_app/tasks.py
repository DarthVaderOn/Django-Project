from time import sleep
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_task():
    sleep(10)
    send_mail('Welcome New User!',
    'This is proof the task worked!',
    '',        # Enter your email address
    [''])      # Enter his email address

    return None