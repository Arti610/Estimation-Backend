# Generated by Django 3.2.19 on 2023-08-22 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
