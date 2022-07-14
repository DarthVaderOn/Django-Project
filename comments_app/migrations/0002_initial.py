# Generated by Django 4.0.4 on 2022-07-14 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publication_app', '0001_initial'),
        ('comments_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='publication_app.post'),
        ),
    ]