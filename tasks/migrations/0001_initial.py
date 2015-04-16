# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EveApiCache',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('priority', models.IntegerField(choices=[(0, b'Very Low'), (1, b'Low'), (2, b'Normal'), (3, b'High'), (4, b'Very High')])),
                ('kwargs', picklefield.fields.PickledObjectField(null=True, editable=False, blank=True)),
                ('category', models.CharField(max_length=15, choices=[(b'account', b'Account'), (b'char', b'Char'), (b'corp', b'Corp'), (b'eve', b'Eve'), (b'map', b'Map'), (b'server', b'Server'), (b'API', b'API')])),
                ('key', models.CharField(max_length=254)),
                ('api', models.ForeignKey(to='apis.Api', null=True)),
            ],
            options={
                'ordering': ['-date'],
                'abstract': False,
            },
        ),
    ]
