# Generated by Django 3.1.6 on 2021-02-18 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_auto_20210217_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_description',
            new_name='task_title',
        ),
    ]
