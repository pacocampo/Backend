# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-22 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('destino', '0002_auto_20160219_1802'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='destino',
            managers=[
                ('mexico', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='destino',
            name='imagen',
            field=models.ImageField(upload_to='pais/'),
        ),
    ]
