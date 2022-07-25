from celery import shared_task


@shared_task
def mailing_list_email_task():
    """Рассылка писем о новых записях"""
    return None