# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-08 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0036_auto_20181008_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termshift',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
