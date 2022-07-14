# Generated by Django 4.0.4 on 2022-07-14 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments_app', '0003_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes_app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='likepost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='likecomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_comment', to='comments_app.comments'),
        ),
        migrations.AddField(
            model_name='likecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='likepost',
            unique_together={('post', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='likecomment',
            unique_together={('comment', 'user')},
        ),
    ]
