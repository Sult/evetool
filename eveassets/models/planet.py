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





class Planetschematics(models.Model):
    schematicid = models.SmallIntegerField(db_column='schematicID', primary_key=True)  # Field name made lowercase.
    schematicname = models.TextField(db_column='schematicName', blank=True)  # Field name made lowercase.
    cycletime = models.BigIntegerField(db_column='cycleTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planetSchematics'


class Planetschematicspinmap(models.Model):
    
    schematicid = models.SmallIntegerField(db_column='schematicID')  # Field name made lowercase.
    pintypeid = models.BigIntegerField(db_column='pinTypeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planetSchematicsPinMap'


class Planetschematicstypemap(models.Model):
    
    schematicid = models.SmallIntegerField(db_column='schematicID')  # Field name made lowercase.
    typeid = models.BigIntegerField(db_column='typeID')  # Field name made lowercase.
    quantity = models.SmallIntegerField(blank=True, null=True)
    isinput = models.NullBooleanField(db_column='isInput')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planetSchematicsTypeMap'
