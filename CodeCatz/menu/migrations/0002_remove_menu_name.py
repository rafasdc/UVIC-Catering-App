# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 07:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='name',
        ),
    ]
