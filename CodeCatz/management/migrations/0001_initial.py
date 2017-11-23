# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 23:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
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
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name', max_length=50)),
                ('address', models.CharField(help_text='Enter address', max_length=200)),
                ('phone', models.CharField(help_text='Enter phone number', max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('event', models.ManyToManyField(blank=True, help_text='Assign employee to event', to='events.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('COOOK', 'COOK'), ('WAITER', 'WAITER'), ('DELIVERY', 'DELIVERY')], help_text='Choose role', max_length=15, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ManyToManyField(blank=True, to='management.Role'),
        ),
    ]
