# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyect',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='objetives',
            field=models.ManyToManyField(blank=True, null=True, to='Proyectos.Objetive'),
        ),
        migrations.AlterField(
            model_name='proyect',
            name='obstacles',
            field=models.ManyToManyField(blank=True, null=True, to='Proyectos.Obstacle'),
        ),
    ]