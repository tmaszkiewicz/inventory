# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-18 13:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0045_auto_20181018_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termshift',
            name='eventDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 18, 15, 0, 50, 176694), null=True),
        ),
    ]