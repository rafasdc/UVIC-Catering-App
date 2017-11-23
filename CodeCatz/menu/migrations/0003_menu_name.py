# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_menu_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.CharField(default='', max_length=100, verbose_name='Title'),
            preserve_default=False,
        ),
    ]