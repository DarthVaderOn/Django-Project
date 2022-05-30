# Generated by Django 4.0.4 on 2022-05-29 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags_app', '0003_alter_tag_options_alter_tag_title'),
        ('media_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tags_app.tag', verbose_name='Tags'),
        ),
    ]