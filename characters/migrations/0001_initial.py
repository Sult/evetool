# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import evetool.storage


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterApi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('characterid', models.BigIntegerField()),
                ('charactername', models.CharField(max_length=254)),
                ('corporationid', models.BigIntegerField()),
                ('corporationname', models.CharField(max_length=254)),
                ('api', models.ForeignKey(to='apis.Api')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterApiIcon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.IntegerField(choices=[(b'Tiny', 32), (b'Small', 64), (b'Medium', 128), (b'Large', 256), (b'Huge', 512), (b'Special', 200)])),
                ('typeid', models.IntegerField()),
                ('icon', models.ImageField(storage=evetool.storage.OverwriteStorage(), null=True, upload_to=b'images/characters/', blank=True)),
                ('relation', models.ForeignKey(to='characters.CharacterApi')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterJournal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reftypeid', models.SmallIntegerField()),
                ('ownername1', models.CharField(max_length=254)),
                ('ownerid1', models.IntegerField()),
                ('ownername2', models.CharField(max_length=254)),
                ('ownerid2', models.IntegerField()),
                ('argname1', models.CharField(max_length=254)),
                ('argid1', models.IntegerField()),
                ('amount', models.FloatField(null=True)),
                ('reason', models.TextField(blank=True)),
                ('taxreceiverid', models.IntegerField(null=True)),
                ('taxamount', models.FloatField(null=True)),
                ('date', models.DateTimeField()),
                ('balance', models.FloatField()),
                ('characterapi', models.ForeignKey(to='characters.CharacterApi')),
            ],
            options={
                'ordering': ['-date', '-reftypeid'],
            },
        ),
        migrations.CreateModel(
            name='RefType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reftypeid', models.IntegerField(unique=True)),
                ('reftypename', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='RequiredSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skilllevel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('typeid', models.BigIntegerField(unique=True)),
                ('typename', models.CharField(max_length=254)),
                ('published', models.IntegerField()),
                ('description', models.TextField()),
                ('rank', models.IntegerField()),
                ('primaryattribute', models.CharField(max_length=254)),
                ('secondaryattribute', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='SkillBonus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bonustype', models.CharField(max_length=254)),
                ('bonusvalue', models.FloatField()),
                ('skill', models.ForeignKey(to='characters.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='SkillGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupid', models.BigIntegerField(unique=True)),
                ('groupname', models.CharField(unique=True, max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='skillgroup',
            field=models.ForeignKey(to='characters.SkillGroup'),
        ),
        migrations.AddField(
            model_name='requiredskill',
            name='required',
            field=models.ForeignKey(related_name='required', to='characters.Skill'),
        ),
        migrations.AddField(
            model_name='requiredskill',
            name='skill',
            field=models.ForeignKey(related_name='required_skills', to='characters.Skill'),
        ),
        migrations.AlterUniqueTogether(
            name='characterjournal',
            unique_together=set([('characterapi', 'date', 'balance')]),
        ),
        migrations.AlterUniqueTogether(
            name='characterapiicon',
            unique_together=set([('size', 'relation')]),
        ),
    ]
