# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-09-12 09:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0031_user_samaccountname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='SamAccountName',
            new_name='sAMAccountName',
        ),
    ]