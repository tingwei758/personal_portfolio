# Generated by Django 2.2.3 on 2019-07-04 21:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190704_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 4, 21, 1, 11, 129212, tzinfo=utc)),
        ),
    ]
