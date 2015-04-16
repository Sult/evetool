# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models





class Chrancestries(models.Model):
    ancestryid = models.SmallIntegerField(db_column='ancestryID', primary_key=True)  # Field name made lowercase.
    ancestryname = models.TextField(db_column='ancestryName', blank=True)  # Field name made lowercase.
    bloodlineid = models.SmallIntegerField(db_column='bloodlineID', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    perception = models.SmallIntegerField(blank=True, null=True)
    willpower = models.SmallIntegerField(blank=True, null=True)
    charisma = models.SmallIntegerField(blank=True, null=True)
    memory = models.SmallIntegerField(blank=True, null=True)
    intelligence = models.SmallIntegerField(blank=True, null=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.TextField(db_column='shortDescription', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chrAncestries'


class Chrattributes(models.Model):
    attributeid = models.SmallIntegerField(db_column='attributeID', primary_key=True)  # Field name made lowercase.
    attributename = models.TextField(db_column='attributeName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.TextField(db_column='shortDescription', blank=True)  # Field name made lowercase.
    notes = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'chrAttributes'


class Chrbloodlines(models.Model):
    bloodlineid = models.SmallIntegerField(db_column='bloodlineID', primary_key=True)  # Field name made lowercase.
    bloodlinename = models.TextField(db_column='bloodlineName', blank=True)  # Field name made lowercase.
    raceid = models.SmallIntegerField(db_column='raceID', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    maledescription = models.TextField(db_column='maleDescription', blank=True)  # Field name made lowercase.
    femaledescription = models.TextField(db_column='femaleDescription', blank=True)  # Field name made lowercase.
    shiptypeid = models.BigIntegerField(db_column='shipTypeID', blank=True, null=True)  # Field name made lowercase.
    corporationid = models.BigIntegerField(db_column='corporationID', blank=True, null=True)  # Field name made lowercase.
    perception = models.SmallIntegerField(blank=True, null=True)
    willpower = models.SmallIntegerField(blank=True, null=True)
    charisma = models.SmallIntegerField(blank=True, null=True)
    memory = models.SmallIntegerField(blank=True, null=True)
    intelligence = models.SmallIntegerField(blank=True, null=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.TextField(db_column='shortDescription', blank=True)  # Field name made lowercase.
    shortmaledescription = models.TextField(db_column='shortMaleDescription', blank=True)  # Field name made lowercase.
    shortfemaledescription = models.TextField(db_column='shortFemaleDescription', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chrBloodlines'


class Chrfactions(models.Model):
    factionid = models.BigIntegerField(db_column='factionID', primary_key=True)  # Field name made lowercase.
    factionname = models.TextField(db_column='factionName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    raceids = models.BigIntegerField(db_column='raceIDs', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.BigIntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    corporationid = models.BigIntegerField(db_column='corporationID', blank=True, null=True)  # Field name made lowercase.
    sizefactor = models.FloatField(db_column='sizeFactor', blank=True, null=True)  # Field name made lowercase.
    stationcount = models.SmallIntegerField(db_column='stationCount', blank=True, null=True)  # Field name made lowercase.
    stationsystemcount = models.SmallIntegerField(db_column='stationSystemCount', blank=True, null=True)  # Field name made lowercase.
    militiacorporationid = models.BigIntegerField(db_column='militiaCorporationID', blank=True, null=True)  # Field name made lowercase.
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chrFactions'


class Chrraces(models.Model):
    raceid = models.SmallIntegerField(db_column='raceID', primary_key=True)  # Field name made lowercase.
    racename = models.TextField(db_column='raceName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.TextField(db_column='shortDescription', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chrRaces'
