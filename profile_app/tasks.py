import os
from pathlib import Path
from time import sleep
from celery import shared_task
from django.core.mail import send_mail
from dotenv import load_dotenv


load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


@shared_task
def send_email_task():
    sleep(10)
    send_mail('Welcome New User!',
    'This is proof the task worked!',
    str(os.getenv('EMAIL_HOST_USER')),        # Enter your email address
    [''])                                     # Enter his email address

    return None