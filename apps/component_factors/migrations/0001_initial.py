# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HandlebarOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
            options={
                'ordering': ['option'],
            },
        ),
        migrations.CreateModel(
            name='SaddleOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
            options={
                'ordering': ['option'],
            },
        ),
    ]