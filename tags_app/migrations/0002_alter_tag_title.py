# Generated by Django 4.0.4 on 2022-05-29 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=128, unique=True),
        ),
    ]
