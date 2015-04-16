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


class Agtagenttypes(models.Model): 
    agenttypeid = models.BigIntegerField(db_column='agentTypeID', primary_key=True)  # Field name made lowercase.
    agenttype = models.TextField(db_column='agentType', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agtAgentTypes'


class Agtagents(models.Model):
    agentid = models.BigIntegerField(db_column='agentID', primary_key=True)  # Field name made lowercase.
    divisionid = models.SmallIntegerField(db_column='divisionID', blank=True, null=True)  # Field name made lowercase.
    corporationid = models.BigIntegerField(db_column='corporationID', blank=True, null=True)  # Field name made lowercase.
    locationid = models.BigIntegerField(db_column='locationID', blank=True, null=True)  # Field name made lowercase.
    level = models.SmallIntegerField(blank=True, null=True)
    quality = models.SmallIntegerField(blank=True, null=True)
    agenttypeid = models.BigIntegerField(db_column='agentTypeID', blank=True, null=True)  # Field name made lowercase.
    islocator = models.NullBooleanField(db_column='isLocator')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agtAgents'


class Agtresearchagents(models.Model):
    
    agentid = models.BigIntegerField(db_column='agentID')  # Field name made lowercase.
    typeid = models.BigIntegerField(db_column='typeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agtResearchAgents'
