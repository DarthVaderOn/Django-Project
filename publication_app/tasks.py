import os
from celery import shared_task
from datetime import datetime, timedelta
from django.core.mail import send_mail
from publication_app.models import Post
from user_app.models import User


@shared_task
def mailing_list_email_task():
    """Ежедневная рассылка писем о новых записях"""
    start_date = datetime.now() - timedelta(days=1)                                                                                                 # время за последние сутки
    end_date = datetime.now()                                                                                                                       # время сейчас
    new_posts = list(map(lambda p: p.text, Post.objects.filter(created_at__range = [start_date, end_date])))                                        # делаем список, с функцией map() возвращающая объект map (итератор), который мы можем использовать в других частях нашей программы.
                                                                                                                                                    # добавляем lambda с аргументом text поста, фильтруем посты сделаные за сутки.
    if len(new_posts) > 0:
        for spam in User.objects.all():
            send_mail(
                'New Posts!',
                'Posts:\n' + '\n'.join(new_posts) + '\n\nNew and bright posts only on our website. https://django-darth-vader-on.herokuapp.com/',   # преобразовываем список в строку с помощью join()
                str(os.getenv('EMAIL_HOST_USER')),                                                                                                  # Enter your email address
                [spam.email]
            )
    return None