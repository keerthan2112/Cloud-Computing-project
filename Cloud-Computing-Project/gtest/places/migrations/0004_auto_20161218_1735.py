# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-18 22:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20161117_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='guide',
            name='guide_city',
        ),
        migrations.RemoveField(
            model_name='guide',
            name='guide_country',
        ),
        migrations.RemoveField(
            model_name='guide',
            name='guide_dob',
        ),
        migrations.RemoveField(
            model_name='guide',
            name='guide_sex',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_dob',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_sex',
        ),
        migrations.AddField(
            model_name='guide',
            name='guide_number',
            field=models.CharField(default=datetime.datetime(2016, 12, 18, 22, 35, 36, 594541, tzinfo=utc), max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guide',
            name='guide_places',
            field=models.CharField(default=datetime.datetime(2016, 12, 18, 22, 35, 42, 757305, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
