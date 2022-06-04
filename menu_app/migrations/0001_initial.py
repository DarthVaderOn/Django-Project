# Generated by Django 4.0.4 on 2022-06-04 15:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_label', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=256)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='')),
                ('priority', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)])),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='links', to='menu_app.menu')),
            ],
        ),
        migrations.AddIndex(
            model_name='menuitem',
            index=models.Index(fields=['menu'], name='menu_app_me_menu_id_a0f054_idx'),
        ),
        migrations.AddIndex(
            model_name='menuitem',
            index=models.Index(fields=['menu', 'url'], name='menu_app_me_menu_id_131b4b_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='menuitem',
            unique_together={('menu', 'title')},
        ),
    ]
