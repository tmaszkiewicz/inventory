# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-13 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_machine_ou'),
    ]

    operations = [
        migrations.AddField(
            model_name='svr',
            name='OU',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
