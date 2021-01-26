# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-13 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0025_auto_20180706_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(blank=True, max_length=30)),
                ('hostname', models.CharField(blank=True, max_length=30)),
                ('model', models.CharField(blank=True, max_length=30)),
                ('mac', models.CharField(blank=True, max_length=20)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('dep', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]