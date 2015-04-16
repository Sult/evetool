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





class Mapcelestialstatistics(models.Model):
    celestialid = models.BigIntegerField(db_column='celestialID', primary_key=True)  # Field name made lowercase.
    temperature = models.FloatField(blank=True, null=True)
    spectralclass = models.TextField(db_column='spectralClass', blank=True)  # Field name made lowercase.
    luminosity = models.FloatField(blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    life = models.FloatField(blank=True, null=True)
    orbitradius = models.FloatField(db_column='orbitRadius', blank=True, null=True)  # Field name made lowercase.
    eccentricity = models.FloatField(blank=True, null=True)
    massdust = models.FloatField(db_column='massDust', blank=True, null=True)  # Field name made lowercase.
    massgas = models.FloatField(db_column='massGas', blank=True, null=True)  # Field name made lowercase.
    fragmented = models.BigIntegerField(blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    surfacegravity = models.FloatField(db_column='surfaceGravity', blank=True, null=True)  # Field name made lowercase.
    escapevelocity = models.FloatField(db_column='escapeVelocity', blank=True, null=True)  # Field name made lowercase.
    orbitperiod = models.FloatField(db_column='orbitPeriod', blank=True, null=True)  # Field name made lowercase.
    rotationrate = models.FloatField(db_column='rotationRate', blank=True, null=True)  # Field name made lowercase.
    locked = models.BigIntegerField(blank=True, null=True)
    pressure = models.BigIntegerField(blank=True, null=True)
    radius = models.BigIntegerField(blank=True, null=True)
    mass = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapCelestialStatistics'


class Mapconstellationjumps(models.Model):
    
    fromregionid = models.BigIntegerField(db_column='fromRegionID', blank=True, null=True)  # Field name made lowercase.
    fromconstellationid = models.BigIntegerField(db_column='fromConstellationID')  # Field name made lowercase.
    toconstellationid = models.BigIntegerField(db_column='toConstellationID')  # Field name made lowercase.
    toregionid = models.BigIntegerField(db_column='toRegionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapConstellationJumps'


class Mapconstellations(models.Model):
    regionid = models.BigIntegerField(db_column='regionID', blank=True, null=True)  # Field name made lowercase.
    constellationid = models.BigIntegerField(db_column='constellationID', primary_key=True)  # Field name made lowercase.
    constellationname = models.TextField(db_column='constellationName', blank=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True)  # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax', blank=True, null=True)  # Field name made lowercase.
    ymin = models.FloatField(db_column='yMin', blank=True, null=True)  # Field name made lowercase.
    ymax = models.FloatField(db_column='yMax', blank=True, null=True)  # Field name made lowercase.
    zmin = models.FloatField(db_column='zMin', blank=True, null=True)  # Field name made lowercase.
    zmax = models.FloatField(db_column='zMax', blank=True, null=True)  # Field name made lowercase.
    factionid = models.BigIntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.
    radius = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapConstellations'


class Mapdenormalize(models.Model):
    itemid = models.BigIntegerField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    typeid = models.BigIntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    groupid = models.BigIntegerField(db_column='groupID', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.BigIntegerField(db_column='solarSystemID', blank=True, null=True)  # Field name made lowercase.
    constellationid = models.BigIntegerField(db_column='constellationID', blank=True, null=True)  # Field name made lowercase.
    regionid = models.BigIntegerField(db_column='regionID', blank=True, null=True)  # Field name made lowercase.
    orbitid = models.BigIntegerField(db_column='orbitID', blank=True, null=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    itemname = models.TextField(db_column='itemName', blank=True)  # Field name made lowercase.
    security = models.FloatField(blank=True, null=True)
    celestialindex = models.BigIntegerField(db_column='celestialIndex', blank=True, null=True)  # Field name made lowercase.
    orbitindex = models.BigIntegerField(db_column='orbitIndex', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapDenormalize'


class Mapjumps(models.Model):
    stargateid = models.BigIntegerField(db_column='stargateID', primary_key=True)  # Field name made lowercase.
    destinationid = models.BigIntegerField(db_column='destinationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapJumps'


class Maplandmarks(models.Model):
    landmarkid = models.BigIntegerField(db_column='landmarkID', primary_key=True)  # Field name made lowercase.
    landmarkname = models.TextField(db_column='landmarkName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    locationid = models.BigIntegerField(db_column='locationID', blank=True, null=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapLandmarks'


class Maplocationscenes(models.Model):
    locationid = models.BigIntegerField(db_column='locationID', primary_key=True)  # Field name made lowercase.
    graphicid = models.BigIntegerField(db_column='graphicID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapLocationScenes'


class Maplocationwormholeclasses(models.Model):
    locationid = models.BigIntegerField(db_column='locationID', primary_key=True)  # Field name made lowercase.
    wormholeclassid = models.BigIntegerField(db_column='wormholeClassID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapLocationWormholeClasses'


class Mapregionjumps(models.Model):
    
    fromregionid = models.BigIntegerField(db_column='fromRegionID')  # Field name made lowercase.
    toregionid = models.BigIntegerField(db_column='toRegionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapRegionJumps'


class Mapregions(models.Model):
    regionid = models.BigIntegerField(db_column='regionID', primary_key=True)  # Field name made lowercase.
    regionname = models.TextField(db_column='regionName', blank=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True)  # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax', blank=True, null=True)  # Field name made lowercase.
    ymin = models.FloatField(db_column='yMin', blank=True, null=True)  # Field name made lowercase.
    ymax = models.FloatField(db_column='yMax', blank=True, null=True)  # Field name made lowercase.
    zmin = models.FloatField(db_column='zMin', blank=True, null=True)  # Field name made lowercase.
    zmax = models.FloatField(db_column='zMax', blank=True, null=True)  # Field name made lowercase.
    factionid = models.BigIntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.
    radius = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapRegions'


class Mapsolarsystemjumps(models.Model):
    
    fromregionid = models.BigIntegerField(db_column='fromRegionID', blank=True, null=True)  # Field name made lowercase.
    fromconstellationid = models.BigIntegerField(db_column='fromConstellationID', blank=True, null=True)  # Field name made lowercase.
    fromsolarsystemid = models.BigIntegerField(db_column='fromSolarSystemID')  # Field name made lowercase.
    tosolarsystemid = models.BigIntegerField(db_column='toSolarSystemID')  # Field name made lowercase.
    toconstellationid = models.BigIntegerField(db_column='toConstellationID', blank=True, null=True)  # Field name made lowercase.
    toregionid = models.BigIntegerField(db_column='toRegionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapSolarSystemJumps'


class Mapsolarsystems(models.Model):
    regionid = models.BigIntegerField(db_column='regionID', blank=True, null=True)  # Field name made lowercase.
    constellationid = models.BigIntegerField(db_column='constellationID', blank=True, null=True)  # Field name made lowercase.
    solarsystemid = models.BigIntegerField(db_column='solarSystemID', primary_key=True)  # Field name made lowercase.
    solarsystemname = models.TextField(db_column='solarSystemName', blank=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True)  # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax', blank=True, null=True)  # Field name made lowercase.
    ymin = models.FloatField(db_column='yMin', blank=True, null=True)  # Field name made lowercase.
    ymax = models.FloatField(db_column='yMax', blank=True, null=True)  # Field name made lowercase.
    zmin = models.FloatField(db_column='zMin', blank=True, null=True)  # Field name made lowercase.
    zmax = models.FloatField(db_column='zMax', blank=True, null=True)  # Field name made lowercase.
    luminosity = models.FloatField(blank=True, null=True)
    border = models.SmallIntegerField(blank=True, null=True)
    fringe = models.SmallIntegerField(blank=True, null=True)
    corridor = models.SmallIntegerField(blank=True, null=True)
    hub = models.SmallIntegerField(blank=True, null=True)
    international = models.SmallIntegerField(blank=True, null=True)
    regional = models.SmallIntegerField(blank=True, null=True)
    constellation = models.SmallIntegerField(blank=True, null=True)
    security = models.FloatField(blank=True, null=True)
    factionid = models.BigIntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.
    radius = models.FloatField(blank=True, null=True)
    suntypeid = models.BigIntegerField(db_column='sunTypeID', blank=True, null=True)  # Field name made lowercase.
    securityclass = models.TextField(db_column='securityClass', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mapSolarSystems'


class Mapuniverse(models.Model):
    universeid = models.BigIntegerField(db_column='universeID', primary_key=True)  # Field name made lowercase.
    universename = models.TextField(db_column='universeName', blank=True)  # Field name made lowercase.
    x = models.FloatField(blank=True, null=True)
    y = models.FloatField(blank=True, null=True)
    z = models.FloatField(blank=True, null=True)
    xmin = models.FloatField(db_column='xMin', blank=True, null=True)  # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax', blank=True, null=True)  # Field name made lowercase.
    ymin = models.FloatField(db_column='yMin', blank=True, null=True)  # Field name made lowercase.
    ymax = models.FloatField(db_column='yMax', blank=True, null=True)  # Field name made lowercase.
    zmin = models.FloatField(db_column='zMin', blank=True, null=True)  # Field name made lowercase.
    zmax = models.FloatField(db_column='zMax', blank=True, null=True)  # Field name made lowercase.
    radius = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mapUniverse'
