# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-22 12:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0052_auto_20181022_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foamrow',
            name='plant',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='termshift',
            name='eventDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 22, 14, 1, 22, 276532), null=True),
        ),
    ]