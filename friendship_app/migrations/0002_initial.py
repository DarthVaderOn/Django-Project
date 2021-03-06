# Generated by Django 4.0.4 on 2022-07-14 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('friendship_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='friendshiprequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship_request', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friendshiprequest',
            name='user_invite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendship', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_request', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followrequest',
            name='user_follow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='friendshiprequest',
            unique_together={('user', 'user_invite')},
        ),
        migrations.AlterUniqueTogether(
            name='followrequest',
            unique_together={('user', 'user_follow')},
        ),
    ]
