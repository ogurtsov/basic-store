# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20171020_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]
