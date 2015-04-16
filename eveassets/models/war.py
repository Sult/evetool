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





class Warcombatzonesystems(models.Model):
    solarsystemid = models.BigIntegerField(db_column='solarSystemID', primary_key=True)  # Field name made lowercase.
    combatzoneid = models.BigIntegerField(db_column='combatZoneID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'warCombatZoneSystems'


class Warcombatzones(models.Model):
    combatzoneid = models.BigIntegerField(db_column='combatZoneID', primary_key=True)  # Field name made lowercase.
    combatzonename = models.TextField(db_column='combatZoneName', blank=True)  # Field name made lowercase.
    factionid = models.BigIntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.
    centersystemid = models.BigIntegerField(db_column='centerSystemID', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'warCombatZones'
