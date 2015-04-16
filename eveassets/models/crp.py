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




class Crpactivities(models.Model):
    activityid = models.SmallIntegerField(db_column='activityID', primary_key=True)  # Field name made lowercase.
    activityname = models.TextField(db_column='activityName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'crpActivities'


class Crpnpccorporationdivisions(models.Model):
    
    corporationid = models.BigIntegerField(db_column='corporationID')  # Field name made lowercase.
    divisionid = models.SmallIntegerField(db_column='divisionID')  # Field name made lowercase.
    size = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crpNPCCorporationDivisions'


class Crpnpccorporationresearchfields(models.Model):
    
    skillid = models.BigIntegerField(db_column='skillID')  # Field name made lowercase.
    corporationid = models.BigIntegerField(db_column='corporationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crpNPCCorporationResearchFields'


class Crpnpccorporationtrades(models.Model):
    
    corporationid = models.BigIntegerField(db_column='corporationID')  # Field name made lowercase.
    typeid = models.BigIntegerField(db_column='typeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crpNPCCorporationTrades'


class Crpnpccorporations(models.Model):
    corporationid = models.BigIntegerField(db_column='corporationID', primary_key=True)  # Field name made lowercase.
    size = models.CharField(max_length=1, blank=True)
    extent = models.CharField(max_length=1, blank=True)
    solarsystemid = models.BigIntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    investorid1 = models.BigIntegerField(db_column='investorID1', blank=True, null=True)  # Field name made lowercase.
    investorshares1 = models.SmallIntegerField(db_column='investorShares1', blank=True, null=True)  # Field name made lowercase.
    investorid2 = models.BigIntegerField(db_column='investorID2', blank=True, null=True)  # Field name made lowercase.
    investorshares2 = models.SmallIntegerField(db_column='investorShares2', blank=True, null=True)  # Field name made lowercase.
    investorid3 = models.BigIntegerField(db_column='investorID3', blank=True, null=True)  # Field name made lowercase.
    investorshares3 = models.SmallIntegerField(db_column='investorShares3', blank=True, null=True)  # Field name made lowercase.
    investorid4 = models.BigIntegerField(db_column='investorID4', blank=True, null=True)  # Field name made lowercase.
    investorshares4 = models.SmallIntegerField(db_column='investorShares4', blank=True, null=True)  # Field name made lowercase.
    friendid = models.BigIntegerField(db_column='friendID', blank=True, null=True)  # Field name made lowercase.
    enemyid = models.BigIntegerField(db_column='enemyID', blank=True, null=True)  # Field name made lowercase.
    publicshares = models.BigIntegerField(db_column='publicShares', blank=True, null=True)  # Field name made lowercase.
    initialprice = models.BigIntegerField(db_column='initialPrice', blank=True, null=True)  # Field name made lowercase.
    minsecurity = models.FloatField(db_column='minSecurity', blank=True, null=True)  # Field name made lowercase.
    scattered = models.NullBooleanField()
    fringe = models.SmallIntegerField(blank=True, null=True)
    corridor = models.SmallIntegerField(blank=True, null=True)
    hub = models.SmallIntegerField(blank=True, null=True)
    border = models.SmallIntegerField(blank=True, null=True)
    factionid = models.BigIntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.
    sizefactor = models.FloatField(db_column='sizeFactor', blank=True, null=True)  # Field name made lowercase.
    stationcount = models.SmallIntegerField(db_column='stationCount', blank=True, null=True)  # Field name made lowercase.
    stationsystemcount = models.SmallIntegerField(db_column='stationSystemCount', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crpNPCCorporations'


class Crpnpcdivisions(models.Model):
    divisionid = models.SmallIntegerField(db_column='divisionID', primary_key=True)  # Field name made lowercase.
    divisionname = models.TextField(db_column='divisionName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    leadertype = models.TextField(db_column='leaderType', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'crpNPCDivisions'
