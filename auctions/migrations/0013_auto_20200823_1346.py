# Generated by Django 3.1 on 2020-08-23 12:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20200823_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 12, 46, 8, 733451, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 12, 46, 8, 733451, tzinfo=utc)),
        ),
    ]