# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-17 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_from', models.DateTimeField(verbose_name='booking from')),
                ('booking_to', models.DateTimeField(verbose_name='booking to')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide_name', models.CharField(max_length=200)),
                ('guide_sex', models.CharField(max_length=10)),
                ('guide_dob', models.DateTimeField(verbose_name='date of birth')),
                ('guide_rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='GuideAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.City')),
                ('guide_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Guide')),
            ],
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot_name', models.CharField(max_length=200)),
                ('spot_address', models.CharField(max_length=200)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.City')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_sex', models.CharField(max_length=10)),
                ('user_dob', models.DateTimeField(verbose_name='date of birth')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Country'),
        ),
        migrations.AddField(
            model_name='booking',
            name='guide_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Guide'),
        ),
        migrations.AddField(
            model_name='booking',
            name='spot_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Spot'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.User'),
        ),
    ]