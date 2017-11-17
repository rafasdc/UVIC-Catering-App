# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20171116_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='startTime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
