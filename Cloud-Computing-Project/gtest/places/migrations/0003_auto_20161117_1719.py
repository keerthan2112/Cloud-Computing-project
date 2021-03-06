# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20161117_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_from',
            field=models.DateField(verbose_name='booking from'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_to',
            field=models.DateField(verbose_name='booking to'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='guide_dob',
            field=models.DateField(verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_dob',
            field=models.DateField(verbose_name='date of birth'),
        ),
    ]
