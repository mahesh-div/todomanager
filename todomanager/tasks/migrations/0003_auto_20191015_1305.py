# Generated by Django 2.2.6 on 2019-10-15 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20191015_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 22, 13, 5, 12, 322749)),
        ),
    ]
