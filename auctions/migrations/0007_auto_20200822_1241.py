# Generated by Django 3.1 on 2020-08-22 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='auction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='auctions.auction'),
        ),
    ]