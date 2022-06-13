# Generated by Django 4.0.4 on 2022-06-12 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Messenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.SET_NUll, to='media_app.mediafile')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
