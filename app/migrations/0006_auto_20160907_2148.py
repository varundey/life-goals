# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 21:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160907_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
