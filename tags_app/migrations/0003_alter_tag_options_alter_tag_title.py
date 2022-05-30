# Generated by Django 4.0.4 on 2022-05-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags_app', '0002_alter_tag_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tag'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=128, unique=True, verbose_name='Tag'),
        ),
    ]
