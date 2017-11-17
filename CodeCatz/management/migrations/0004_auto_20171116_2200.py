# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20171116_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='expertise',
            field=models.ManyToManyField(help_text='Assign role to employee', to='management.Role'),
        ),
    ]
