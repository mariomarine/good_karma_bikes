# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customsku',
            name='customSku',
            field=models.CharField(max_length=13),
        ),
    ]
