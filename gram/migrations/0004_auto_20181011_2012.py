# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-11 17:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0003_auto_20181009_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='pimage',
            new_name='image',
        ),
    ]