# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-22 11:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0051_auto_20181022_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='foamrow',
            name='kol17',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='foamrow',
            name='kol18',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='foamrow',
            name='kol19',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='foamrow',
            name='IndexSapNazwa',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='termshift',
            name='eventDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 22, 13, 34, 31, 201458), null=True),
        ),
    ]
