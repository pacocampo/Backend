# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-22 03:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('destino', '0004_auto_20160222_0035'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='destino',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='destino',
            name='imagen',
            field=models.ImageField(upload_to='pais/'),
        ),
    ]