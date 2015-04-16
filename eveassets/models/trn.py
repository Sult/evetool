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




class Translationtables(models.Model):
    
    sourcetable = models.TextField(db_column='sourceTable')  # Field name made lowercase.
    destinationtable = models.TextField(db_column='destinationTable', blank=True)  # Field name made lowercase.
    translatedkey = models.TextField(db_column='translatedKey')  # Field name made lowercase.
    tcgroupid = models.BigIntegerField(db_column='tcGroupID', blank=True, null=True)  # Field name made lowercase.
    tcid = models.BigIntegerField(db_column='tcID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'translationTables'


class Trntranslationcolumns(models.Model):
    tcgroupid = models.SmallIntegerField(db_column='tcGroupID', blank=True, null=True)  # Field name made lowercase.
    tcid = models.SmallIntegerField(db_column='tcID', primary_key=True)  # Field name made lowercase.
    tablename = models.TextField(db_column='tableName')  # Field name made lowercase.
    columnname = models.TextField(db_column='columnName')  # Field name made lowercase.
    masterid = models.TextField(db_column='masterID', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trnTranslationColumns'


class Trntranslationlanguages(models.Model):
    numericlanguageid = models.BigIntegerField(db_column='numericLanguageID', primary_key=True)  # Field name made lowercase.
    languageid = models.TextField(db_column='languageID', blank=True)  # Field name made lowercase.
    languagename = models.TextField(db_column='languageName', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trnTranslationLanguages'


class Trntranslations(models.Model):
    
    tcid = models.SmallIntegerField(db_column='tcID')  # Field name made lowercase.
    keyid = models.BigIntegerField(db_column='keyID')  # Field name made lowercase.
    languageid = models.TextField(db_column='languageID')  # Field name made lowercase.
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'trnTranslations'
