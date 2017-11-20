# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0034_auto_20171119_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='event',
            field=models.ManyToManyField(blank=True, help_text='Assign employee to event', to='events.Event'),
        ),
    ]
