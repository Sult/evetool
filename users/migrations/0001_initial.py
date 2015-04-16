# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.NullBooleanField(choices=[(False, b'Corporation'), (True, b'Alliance'), (None, b'Coalition')])),
                ('membership', models.IntegerField(default=0, choices=[(0, b'Free'), (1, b'Silver'), (2, b'Gold'), (3, b'Platinum')])),
                ('created', models.DateField(auto_now_add=True)),
                ('paid_until', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(unique=True, max_length=254)),
                ('key', models.BigIntegerField(null=True)),
                ('ceo', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Directors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account', models.ForeignKey(to='users.Account')),
                ('director', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='directors',
            unique_together=set([('account', 'director')]),
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([('ceo', 'category')]),
        ),
    ]
