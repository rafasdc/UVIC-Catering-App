# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 06:26
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20171116_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name', max_length=50)),
                ('address', models.CharField(help_text='Enter address', max_length=200)),
                ('phone', models.CharField(help_text='Enter phone number', max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
