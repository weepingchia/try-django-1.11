# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-06 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]