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





class Industryactivity(models.Model):
    
    typeid = models.BigIntegerField(db_column='typeID')  # Field name made lowercase.
    time = models.BigIntegerField(blank=True, null=True)
    activityid = models.BigIntegerField(db_column='activityID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'industryActivity'


class Industryactivitymaterials(models.Model):
    
    typeid = models.BigIntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    activityid = models.BigIntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    materialtypeid = models.BigIntegerField(db_column='materialTypeID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.BigIntegerField(blank=True, null=True)
    consume = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industryActivityMaterials'


class Industryactivityprobabilities(models.Model):
    
    typeid = models.BigIntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    activityid = models.BigIntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    producttypeid = models.BigIntegerField(db_column='productTypeID', blank=True, null=True)  # Field name made lowercase.
    probability = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industryActivityProbabilities'


class Industryactivityproducts(models.Model):
    
    typeid = models.BigIntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    activityid = models.BigIntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    producttypeid = models.BigIntegerField(db_column='productTypeID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industryActivityProducts'


class Industryactivityskills(models.Model):
    
    typeid = models.BigIntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    activityid = models.BigIntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    skillid = models.BigIntegerField(db_column='skillID', blank=True, null=True)  # Field name made lowercase.
    level = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industryActivitySkills'


class Industryblueprints(models.Model):
    typeid = models.BigIntegerField(db_column='typeID', primary_key=True)  # Field name made lowercase.
    maxproductionlimit = models.BigIntegerField(db_column='maxProductionLimit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'industryBlueprints'
