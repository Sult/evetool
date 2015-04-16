# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150416_1126'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([]),
        ),
    ]
