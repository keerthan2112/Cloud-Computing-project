# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guideavailability',
            name='city_id',
        ),
        migrations.RemoveField(
            model_name='guideavailability',
            name='guide_id',
        ),
        migrations.RemoveField(
            model_name='spot',
            name='city_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='guide_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='spot_id',
        ),
        migrations.RemoveField(
            model_name='guide',
            name='guide_rating',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_city',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_country',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guide',
            name='guide_city',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guide',
            name='guide_country',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_password',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='GuideAvailability',
        ),
        migrations.DeleteModel(
            name='Spot',
        ),
    ]
