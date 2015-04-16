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





class Ramactivities(models.Model):
    activityid = models.SmallIntegerField(db_column='activityID', primary_key=True)  # Field name made lowercase.
    activityname = models.TextField(db_column='activityName', blank=True)  # Field name made lowercase.
    iconno = models.TextField(db_column='iconNo', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    published = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ramActivities'


class Ramassemblylinestations(models.Model):
    
    stationid = models.BigIntegerField(db_column='stationID')  # Field name made lowercase.
    assemblylinetypeid = models.SmallIntegerField(db_column='assemblyLineTypeID')  # Field name made lowercase.
    quantity = models.SmallIntegerField(blank=True, null=True)
    stationtypeid = models.BigIntegerField(db_column='stationTypeID', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.BigIntegerField(db_column='ownerID', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.BigIntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    regionid = models.BigIntegerField(db_column='regionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ramAssemblyLineStations'


class Ramassemblylinetypedetailpercategory(models.Model):
    
    assemblylinetypeid = models.SmallIntegerField(db_column='assemblyLineTypeID')  # Field name made lowercase.
    categoryid = models.BigIntegerField(db_column='categoryID')  # Field name made lowercase.
    timemultiplier = models.FloatField(db_column='timeMultiplier', blank=True, null=True)  # Field name made lowercase.
    materialmultiplier = models.FloatField(db_column='materialMultiplier', blank=True, null=True)  # Field name made lowercase.
    costmultiplier = models.FloatField(db_column='costMultiplier', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypeDetailPerCategory'


class Ramassemblylinetypedetailpergroup(models.Model):
    
    assemblylinetypeid = models.SmallIntegerField(db_column='assemblyLineTypeID')  # Field name made lowercase.
    groupid = models.BigIntegerField(db_column='groupID')  # Field name made lowercase.
    timemultiplier = models.FloatField(db_column='timeMultiplier', blank=True, null=True)  # Field name made lowercase.
    materialmultiplier = models.FloatField(db_column='materialMultiplier', blank=True, null=True)  # Field name made lowercase.
    costmultiplier = models.FloatField(db_column='costMultiplier', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypeDetailPerGroup'


class Ramassemblylinetypes(models.Model):
    assemblylinetypeid = models.SmallIntegerField(db_column='assemblyLineTypeID', primary_key=True)  # Field name made lowercase.
    assemblylinetypename = models.TextField(db_column='assemblyLineTypeName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    basetimemultiplier = models.FloatField(db_column='baseTimeMultiplier', blank=True, null=True)  # Field name made lowercase.
    basematerialmultiplier = models.FloatField(db_column='baseMaterialMultiplier', blank=True, null=True)  # Field name made lowercase.
    basecostmultiplier = models.FloatField(db_column='baseCostMultiplier', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(blank=True, null=True)
    activityid = models.SmallIntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    mincostperhour = models.FloatField(db_column='minCostPerHour', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ramAssemblyLineTypes'


class Raminstallationtypecontents(models.Model):
    
    installationtypeid = models.BigIntegerField(db_column='installationTypeID')  # Field name made lowercase.
    assemblylinetypeid = models.SmallIntegerField(db_column='assemblyLineTypeID')  # Field name made lowercase.
    quantity = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ramInstallationTypeContents'
