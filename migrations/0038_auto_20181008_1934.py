# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-08 17:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0037_auto_20181008_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='termshift',
            old_name='date',
            new_name='eventDate',
        ),
    ]
