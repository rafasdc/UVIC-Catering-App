# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(blank=True, choices=[('w', 'Wedding'), ('c', 'Corporate'), ('p', 'Private'), ('s', 'Social'), ('b', 'Bar')], default='s', help_text='Event type.', max_length=1),
        ),
    ]
