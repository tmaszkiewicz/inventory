# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-28 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_svr'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cn',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='distinguishedName',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='memberOf',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='primaryGroupID',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
