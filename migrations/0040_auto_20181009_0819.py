# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-09 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0039_auto_20181009_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termshift',
            name='eventDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
