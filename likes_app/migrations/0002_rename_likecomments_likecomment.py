# Generated by Django 4.0.4 on 2022-06-02 12:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LikeComments',
            new_name='LikeComment',
        ),
    ]
