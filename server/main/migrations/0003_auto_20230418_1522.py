# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2023-04-18 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20230418_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Posts', verbose_name='Должность'),
        ),
    ]
