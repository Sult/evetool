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




class Dgmattributecategories(models.Model):
    categoryid = models.SmallIntegerField(db_column='categoryID', primary_key=True)  # Field name made lowercase.
    categoryname = models.TextField(db_column='categoryName', blank=True)  # Field name made lowercase.
    categorydescription = models.TextField(db_column='categoryDescription', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmAttributeCategories'


class Dgmattributetypes(models.Model):
    attributeid = models.SmallIntegerField(db_column='attributeID', primary_key=True)  # Field name made lowercase.
    attributename = models.TextField(db_column='attributeName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    defaultvalue = models.FloatField(db_column='defaultValue', blank=True, null=True)  # Field name made lowercase.
    published = models.NullBooleanField()
    displayname = models.TextField(db_column='displayName', blank=True)  # Field name made lowercase.
    unitid = models.SmallIntegerField(db_column='unitID', blank=True, null=True)  # Field name made lowercase.
    stackable = models.NullBooleanField()
    highisgood = models.NullBooleanField(db_column='highIsGood')  # Field name made lowercase.
    categoryid = models.SmallIntegerField(db_column='categoryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmAttributeTypes'


class Dgmeffects(models.Model):
    effectid = models.SmallIntegerField(db_column='effectID', primary_key=True)  # Field name made lowercase.
    effectname = models.TextField(db_column='effectName', blank=True)  # Field name made lowercase.
    effectcategory = models.SmallIntegerField(db_column='effectCategory', blank=True, null=True)  # Field name made lowercase.
    preexpression = models.BigIntegerField(db_column='preExpression', blank=True, null=True)  # Field name made lowercase.
    postexpression = models.BigIntegerField(db_column='postExpression', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    guid = models.TextField(blank=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    isoffensive = models.NullBooleanField(db_column='isOffensive')  # Field name made lowercase.
    isassistance = models.NullBooleanField(db_column='isAssistance')  # Field name made lowercase.
    durationattributeid = models.SmallIntegerField(db_column='durationAttributeID', blank=True, null=True)  # Field name made lowercase.
    trackingspeedattributeid = models.SmallIntegerField(db_column='trackingSpeedAttributeID', blank=True, null=True)  # Field name made lowercase.
    dischargeattributeid = models.SmallIntegerField(db_column='dischargeAttributeID', blank=True, null=True)  # Field name made lowercase.
    rangeattributeid = models.SmallIntegerField(db_column='rangeAttributeID', blank=True, null=True)  # Field name made lowercase.
    falloffattributeid = models.SmallIntegerField(db_column='falloffAttributeID', blank=True, null=True)  # Field name made lowercase.
    disallowautorepeat = models.NullBooleanField(db_column='disallowAutoRepeat')  # Field name made lowercase.
    published = models.NullBooleanField()
    displayname = models.TextField(db_column='displayName', blank=True)  # Field name made lowercase.
    iswarpsafe = models.NullBooleanField(db_column='isWarpSafe')  # Field name made lowercase.
    rangechance = models.NullBooleanField(db_column='rangeChance')  # Field name made lowercase.
    electronicchance = models.NullBooleanField(db_column='electronicChance')  # Field name made lowercase.
    propulsionchance = models.NullBooleanField(db_column='propulsionChance')  # Field name made lowercase.
    distribution = models.SmallIntegerField(blank=True, null=True)
    sfxname = models.TextField(db_column='sfxName', blank=True)  # Field name made lowercase.
    npcusagechanceattributeid = models.SmallIntegerField(db_column='npcUsageChanceAttributeID', blank=True, null=True)  # Field name made lowercase.
    npcactivationchanceattributeid = models.SmallIntegerField(db_column='npcActivationChanceAttributeID', blank=True, null=True)  # Field name made lowercase.
    fittingusagechanceattributeid = models.SmallIntegerField(db_column='fittingUsageChanceAttributeID', blank=True, null=True)  # Field name made lowercase.
    modifierinfo = models.TextField(db_column='modifierInfo', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmEffects'


class Dgmexpressions(models.Model):
    expressionid = models.BigIntegerField(db_column='expressionID', primary_key=True)  # Field name made lowercase.
    operandid = models.BigIntegerField(db_column='operandID', blank=True, null=True)  # Field name made lowercase.
    arg1 = models.BigIntegerField(blank=True, null=True)
    arg2 = models.BigIntegerField(blank=True, null=True)
    expressionvalue = models.TextField(db_column='expressionValue', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    expressionname = models.TextField(db_column='expressionName', blank=True)  # Field name made lowercase.
    expressiontypeid = models.BigIntegerField(db_column='expressionTypeID', blank=True, null=True)  # Field name made lowercase.
    expressiongroupid = models.SmallIntegerField(db_column='expressionGroupID', blank=True, null=True)  # Field name made lowercase.
    expressionattributeid = models.SmallIntegerField(db_column='expressionAttributeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmExpressions'


class Dgmtypeattributes(models.Model):
    
    typeid = models.BigIntegerField(db_column='typeID')  # Field name made lowercase.
    attributeid = models.SmallIntegerField(db_column='attributeID')  # Field name made lowercase.
    valueint = models.BigIntegerField(db_column='valueInt', blank=True, null=True)  # Field name made lowercase.
    valuefloat = models.FloatField(db_column='valueFloat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmTypeAttributes'


class Dgmtypeeffects(models.Model):
    
    typeid = models.BigIntegerField(db_column='typeID')  # Field name made lowercase.
    effectid = models.SmallIntegerField(db_column='effectID')  # Field name made lowercase.
    isdefault = models.NullBooleanField(db_column='isDefault')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dgmTypeEffects'
