# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-07 07:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_auto_20180206_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='ip',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]