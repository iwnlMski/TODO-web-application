# Generated by Django 3.1.6 on 2021-02-12 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_auto_20210208_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_to_be_done',
            new_name='task_description',
        ),
    ]
