# Generated by Django 3.1 on 2020-09-13 13:52

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auto_20200913_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 13, 13, 52, 18, 632698, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='auction',
            name='watch_list',
            field=models.ManyToManyField(blank=True, related_name='follow', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 13, 13, 52, 18, 634700, tzinfo=utc)),
        ),
    ]
