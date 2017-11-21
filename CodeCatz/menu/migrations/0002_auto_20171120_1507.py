# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipequantity',
            name='recipe',
        ),
        migrations.AddField(
            model_name='menu',
            name='quantity',
            field=models.IntegerField(default=1, help_text='How many times shall we repeat this menu?', verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='menu_constituents',
            field=models.ManyToManyField(to='menu.Recipe'),
        ),
        migrations.DeleteModel(
            name='RecipeQuantity',
        ),
    ]
