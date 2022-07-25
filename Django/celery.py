import os
from celery import Celery
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')

app = Celery('Django')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.

app.autodiscover_tasks()


#app.conf.beat_schedule = {
#    # Executes every day night at 0:00 a.m.
#    'send-every-day-night': {
#        'task': 'publication_app.tasks.mailing_list_email_task',
#        'schedule': crontab(minute=0, hour=0),
#    },
#}