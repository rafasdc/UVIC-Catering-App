# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0025_auto_20171117_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='assigned_role',
            field=models.ManyToManyField(default=1, to='management.Role'),
        ),
    ]
