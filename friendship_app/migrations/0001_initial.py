# Generated by Django 4.0.4 on 2022-06-16 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendshipRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendship_result', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_request', to=settings.AUTH_USER_MODEL)),
                ('user_invite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FollowRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_request', to=settings.AUTH_USER_MODEL)),
                ('user_follow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
