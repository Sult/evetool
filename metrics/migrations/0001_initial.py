# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alliance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=254)),
                ('shortname', models.CharField(max_length=254)),
                ('allianceid', models.BigIntegerField(unique=True)),
                ('executorcorpid', models.BigIntegerField()),
                ('membercount', models.IntegerField()),
                ('startdate', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastrefresh', models.DateTimeField(null=True)),
                ('characterid', models.BigIntegerField(unique=True)),
                ('charactername', models.CharField(unique=True, max_length=254)),
                ('corporationid', models.BigIntegerField()),
                ('corporationname', models.CharField(max_length=254, blank=True)),
                ('corporationdate', models.DateTimeField(null=True)),
                ('allianceid', models.BigIntegerField(null=True)),
                ('alliancedate', models.DateTimeField(null=True)),
                ('securitystatus', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastrefresh', models.DateTimeField(null=True)),
                ('corporationid', models.BigIntegerField(unique=True)),
                ('corporationname', models.CharField(unique=True, max_length=254)),
                ('ticker', models.CharField(max_length=254)),
                ('isnpccorp', models.BooleanField(default=False)),
                ('allianceid', models.BigIntegerField(null=True)),
                ('alliancename', models.CharField(max_length=254, blank=True)),
                ('avgsecstatus', models.FloatField(default=0.0)),
                ('ceoid', models.BigIntegerField()),
                ('ceoname', models.CharField(max_length=254)),
                ('stationid', models.BigIntegerField()),
                ('description', models.TextField()),
                ('url', models.URLField(max_length=254)),
                ('taxrate', models.FloatField()),
                ('membercount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sovereignty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('solarsystemid', models.BigIntegerField(unique=True)),
                ('solarsystemname', models.CharField(unique=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='SovereigntyHolder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allianceid', models.BigIntegerField(null=True)),
                ('corporationid', models.BigIntegerField(null=True)),
                ('factionid', models.BigIntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sovereignty', models.ForeignKey(to='metrics.Sovereignty')),
            ],
        ),
    ]
