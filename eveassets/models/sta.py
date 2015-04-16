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





class Staoperationservices(models.Model):
    
    operationid = models.SmallIntegerField(db_column='operationID')  # Field name made lowercase.
    serviceid = models.BigIntegerField(db_column='serviceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staOperationServices'


class Staoperations(models.Model):
    activityid = models.SmallIntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    operationid = models.SmallIntegerField(db_column='operationID', primary_key=True)  # Field name made lowercase.
    operationname = models.TextField(db_column='operationName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    fringe = models.SmallIntegerField(blank=True, null=True)
    corridor = models.SmallIntegerField(blank=True, null=True)
    hub = models.SmallIntegerField(blank=True, null=True)
    border = models.SmallIntegerField(blank=True, null=True)
    ratio = models.SmallIntegerField(blank=True, null=True)
    caldaristationtypeid = models.BigIntegerField(db_column='caldariStationTypeID', blank=True, null=True)  # Field name made lowercase.
    minmatarstationtypeid = models.BigIntegerField(db_column='minmatarStationTypeID', blank=True, null=True)  # Field name made lowercase.
    amarrstationtypeid = models.BigIntegerField(db_column='amarrStationTypeID', blank=True, null=True)  # Field name made lowercase.
    gallentestationtypeid = models.BigIntegerField(db_column='gallenteStationTypeID', blank=True, null=True)  # Field name made lowercase.
    jovestationtypeid = models.BigIntegerField(db_column='joveStationTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staOperations'


class Staservices(models.Model):
    serviceid = models.BigIntegerField(db_column='serviceID', primary_key=True)  # Field name made lowercase.
    servicename = models.TextField(db_column='serviceName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'staServices'


class Stastationtypes(models.Model):
    stationtypeid = models.BigIntegerField(db_column='stationTypeID', primary_key=True)  # Field name made lowercase.
    dockentryx = models.FloatField(db_column='dockEntryX', blank=True, null=True)  # Field name made lowercase.
    dockentryy = models.FloatField(db_column='dockEntryY', blank=True, null=True)  # Field name made lowercase.
    dockentryz = models.FloatField(db_column='dockEntryZ', blank=True, null=True)  # Field name made lowercase.
    dockorientationx = models.FloatField(db_column='dockOrientationX', blank=True, null=True)  # Field name made lowercase.
    dockorientationy = models.FloatField(db_column='dockOrientationY', blank=True, null=True)  # Field name made lowercase.
    dockorientationz = models.FloatField(db_column='dockOrientationZ', blank=True, null=True)  # Field name made lowercase.
    operationid = models.SmallIntegerField(db_column='operationID', blank=True, null=True)  # Field name made lowercase.
    officeslots = models.SmallIntegerField(db_column='officeSlots', blank=True, null=True)  # Field name made lowercase.
    reprocessingefficiency = models.FloatField(db_column='reprocessingEfficiency', blank=True, null=True)  # Field name made lowercase.
    conquerable = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'staStationTypes'


class Stastations(models.Model):
    stationid = models.BigIntegerField(db_column='stationID', primary_key=True)  # Field name made lowercase.
    security = models.SmallIntegerField(blank=True, null=True)
    dockingcostpervolume = models.FloatField(db_column='dockingCostPerVolume', blank=True, null=True)  # Field name made lowercase.
    maxshipvolumedockable = models.FloatField(db_column='maxShipVolumeDockable', blank=True, null=True)  # Field name made lowercase.
    officerentalcost = models.BigIntegerField(db_column='officeRentalCost', blank=True, null=True)  # Field name made lowercase.
    operationid = models.SmallIntegerField(db_column='operationID', blank=True, null=True)  # Field name made lowercase.
    stationtypeid = models.BigIntegerField(db_column='stationTypeID', blank=True, null=True)  # Field name made lowercase.
    corporationid = models.BigIntegerField(db_column='corporationID', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.BigIntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    constellationid = models.BigIntegerField(db_column='constellationID', blank=True, null=True)  # Field name made lowercase.
    regionid = models.BigIntegerField(db_column='regionID', blank=True, null=True)  # Field name made lowercase.
    stationname = models.TextField(db_column='stationName', blank=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    reprocessingefficiency = models.FloatField(db_column='reprocessingEfficiency', blank=True, null=True)  # Field name made lowercase.
    reprocessingstationstake = models.FloatField(db_column='reprocessingStationsTake', blank=True, null=True)  # Field name made lowercase.
    reprocessinghangarflag = models.SmallIntegerField(db_column='reprocessingHangarFlag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staStations'
