# Generated by Django 3.1 on 2020-08-23 13:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20200823_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('fashion', 'Fashion'), ('tools', 'Tools'), ('toys', 'Toys'), ('electronics', 'Electronics'), ('home accesories', 'Home accessories'), ('books', 'Books')], default='fashion', max_length=64),
        ),
        migrations.AlterField(
            model_name='auction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 13, 11, 43, 878996, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 13, 11, 43, 878996, tzinfo=utc)),
        ),
    ]
