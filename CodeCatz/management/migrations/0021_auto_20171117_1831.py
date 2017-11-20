# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0020_auto_20171117_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(choices=[('COOK', 'Cook'), ('WAITER', 'Waiter'), ('DELIVERY', 'Delivery')], default='None', help_text='Choose role', max_length=15, unique=True),
        ),
    ]
