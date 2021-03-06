# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0006_mainshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20)),
                ('typename', models.CharField(max_length=100)),
                ('childtypenames', models.CharField(max_length=200)),
                ('typesort', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=20)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=100)),
                ('productlongname', models.CharField(max_length=200)),
                ('isxf', models.BooleanField(default=False)),
                ('pmdesc', models.IntegerField(default=0)),
                ('specifics', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('marketprice', models.CharField(max_length=20)),
                ('categoryid', models.CharField(max_length=20)),
                ('childcid', models.CharField(max_length=20)),
                ('childcidname', models.CharField(max_length=100)),
                ('dealerid', models.CharField(max_length=20)),
                ('storenums', models.CharField(max_length=20)),
                ('productnum', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
    ]
