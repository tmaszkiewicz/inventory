# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-18 17:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0047_auto_20181018_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termshift',
            name='eventDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 18, 19, 27, 11, 648812), null=True),
        ),
    ]
