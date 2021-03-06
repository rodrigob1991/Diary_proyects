# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objetive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Obstacle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('difficulty', models.CharField(choices=[('0', ''), ('mild', 'Mild'), ('medium', 'Medium'), ('strong', 'Strong')], default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Proyect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=20)),
                ('goal_time', models.DateField(blank=True, null=True)),
                ('started_time', models.DateField(blank=True, null=True)),
                ('finished', models.BooleanField(default=False, editable=False)),
                ('objetives', models.ManyToManyField(to='Proyectos.Objetive')),
                ('obstacles', models.ManyToManyField(to='Proyectos.Obstacle')),
            ],
        ),
    ]
