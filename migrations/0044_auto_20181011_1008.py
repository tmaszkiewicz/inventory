# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-11 08:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0043_auto_20181009_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termshift',
            name='eventDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 11, 10, 8, 21, 503371), null=True),
        ),
    ]