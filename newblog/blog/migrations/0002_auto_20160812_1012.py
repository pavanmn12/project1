# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-12 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
