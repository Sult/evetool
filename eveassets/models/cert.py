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



class Certcerts(models.Model):
    certid = models.BigIntegerField(db_column='certID', primary_key=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    groupid = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'certCerts'


class Certmasteries(models.Model):
    
    typeid = models.BigIntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    masterylevel = models.BigIntegerField(db_column='masteryLevel', blank=True, null=True)  # Field name made lowercase.
    certid = models.BigIntegerField(db_column='certID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certMasteries'


class Certskills(models.Model):
    
    certid = models.BigIntegerField(db_column='certID', blank=True, null=True)  # Field name made lowercase.
    skillid = models.BigIntegerField(db_column='skillID', blank=True, null=True)  # Field name made lowercase.
    certlevelint = models.BigIntegerField(db_column='certLevelInt', blank=True, null=True)  # Field name made lowercase.
    skilllevel = models.BigIntegerField(db_column='skillLevel', blank=True, null=True)  # Field name made lowercase.
    certleveltext = models.TextField(db_column='certLevelText', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'certSkills'
