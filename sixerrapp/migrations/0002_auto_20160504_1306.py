# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 13:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sixerrapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='avator',
            new_name='avatar',
        ),
    ]
