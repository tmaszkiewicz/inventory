# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-04 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0032_auto_20180912_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='termShift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateIn', models.DateTimeField(blank=True, null=True)),
                ('dateOut', models.DateTimeField(blank=True, null=True)),
                ('hostnameBefore', models.CharField(blank=True, max_length=30, null=True)),
                ('hostnameAfter', models.CharField(blank=True, max_length=30, null=True)),
                ('depBefore', models.CharField(blank=True, max_length=30, null=True)),
                ('depAfter', models.CharField(blank=True, max_length=30, null=True)),
                ('odbierajacy', models.CharField(blank=True, max_length=30, null=True)),
                ('wydajacy', models.CharField(blank=True, max_length=30, null=True)),
                ('term', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.term')),
            ],
        ),
    ]
