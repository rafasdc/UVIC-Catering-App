# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0032_auto_20171119_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.ManyToManyField(blank=True, to='management.Role'),
        ),
    ]
