# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 01:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edziennik', '0002_auto_20160223_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edziennik.StudentClass'),
        ),
    ]
