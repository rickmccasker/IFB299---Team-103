# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20170913_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('departments', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=5, null=True)),
                ('usertype', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'Colleges',
                'verbose_name': 'Colleges',
                'verbose_name_plural': 'Colleges',
            },
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('desc', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=5, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'Hotels',
                'verbose_name': 'Hotels',
                'verbose_name_plural': 'Hotels',
            },
        ),
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('industry_type', models.CharField(blank=True, max_length=60, null=True)),
                ('desc', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=5, null=True)),
                ('usertype', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'Industries',
                'verbose_name': 'Industries',
                'verbose_name_plural': 'Industries',
            },
        ),
        migrations.CreateModel(
            name='Libraries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('desc', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=5, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'Libraries',
                'verbose_name': 'Libraries',
                'verbose_name_plural': 'Libraries',
            },
        ),
        migrations.CreateModel(
            name='Malls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('desc', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=5, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'Malls',
                'verbose_name': 'Malls',
                'verbose_name_plural': 'Malls',
            },
        ),
        migrations.CreateModel(
            name='Museums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('desc', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=5, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'Museums',
                'verbose_name': 'Museums',
                'verbose_name_plural': 'Museums',
            },
        ),
        migrations.CreateModel(
            name='Parks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('desc', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=5, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'Parks',
                'verbose_name': 'Parks',
                'verbose_name_plural': 'Parks',
            },
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('desc', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=5, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'Restaurants',
                'verbose_name': 'Restaurants',
                'verbose_name_plural': 'Restaurants',
            },
        ),
        migrations.CreateModel(
            name='Zoos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('desc', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.CharField(blank=True, max_length=5, null=True)),
                ('type', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'Zoos',
                'verbose_name': 'Zoos',
                'verbose_name_plural': 'Zoos',
            },
        ),
        migrations.DeleteModel(
            name='Service2',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]