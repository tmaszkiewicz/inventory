# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-15 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0028_auto_20180815_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='hostname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='term',
            name='model',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]