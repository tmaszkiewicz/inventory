# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-05 12:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20180605_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='svr',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.user'),
        ),
        migrations.AlterField(
            model_name='svr',
            name='windowsSvrLicense',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.windowsSvrLicense'),
        ),
    ]
