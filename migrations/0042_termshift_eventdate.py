# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-09 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0041_remove_termshift_eventdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='termshift',
            name='eventDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]