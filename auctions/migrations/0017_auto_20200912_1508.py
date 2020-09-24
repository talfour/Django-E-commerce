# Generated by Django 3.1 on 2020-09-12 14:08

import auctions.models
import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20200912_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to=auctions.models.get_upload_path),
        ),
        migrations.AlterField(
            model_name='auction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 14, 8, 7, 325905, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='auction',
            name='title',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='bid',
            name='starting_bid',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 12, 14, 8, 7, 325905, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='image',
            name='auction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='auctions.auction'),
        ),
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.user'),
        ),
    ]
