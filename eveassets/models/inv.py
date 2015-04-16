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





class Invcategories(models.Model):
    categoryid = models.BigIntegerField(db_column='categoryID', primary_key=True)  # Field name made lowercase.
    categoryname = models.TextField(db_column='categoryName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    published = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'invCategories'


class Invcontrabandtypes(models.Model):
    
    factionid = models.BigIntegerField(db_column='factionID')  # Field name made lowercase.
    typeid = models.BigIntegerField(db_column='typeID')  # Field name made lowercase.
    standingloss = models.FloatField(db_column='standingLoss', blank=True, null=True)  # Field name made lowercase.
    confiscateminsec = models.FloatField(db_column='confiscateMinSec', blank=True, null=True)  # Field name made lowercase.
    finebyvalue = models.FloatField(db_column='fineByValue', blank=True, null=True)  # Field name made lowercase.
    attackminsec = models.FloatField(db_column='attackMinSec', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invContrabandTypes'


class Invcontroltowerresourcepurposes(models.Model):
    purpose = models.SmallIntegerField(primary_key=True)
    purposetext = models.TextField(db_column='purposeText', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invControlTowerResourcePurposes'


class Invcontroltowerresources(models.Model):
    
    controltowertypeid = models.BigIntegerField(db_column='controlTowerTypeID')  # Field name made lowercase.
    resourcetypeid = models.BigIntegerField(db_column='resourceTypeID')  # Field name made lowercase.
    purpose = models.SmallIntegerField(blank=True, null=True)
    quantity = models.BigIntegerField(blank=True, null=True)
    minsecuritylevel = models.FloatField(db_column='minSecurityLevel', blank=True, null=True)  # Field name made lowercase.
    factionid = models.BigIntegerField(db_column='factionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invControlTowerResources'


class Invflags(models.Model):
    flagid = models.SmallIntegerField(db_column='flagID', primary_key=True)  # Field name made lowercase.
    flagname = models.TextField(db_column='flagName', blank=True)  # Field name made lowercase.
    flagtext = models.TextField(db_column='flagText', blank=True)  # Field name made lowercase.
    orderid = models.BigIntegerField(db_column='orderID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invFlags'


class Invgroups(models.Model):
    groupid = models.BigIntegerField(db_column='groupID', primary_key=True)  # Field name made lowercase.
    categoryid = models.BigIntegerField(db_column='categoryID', blank=True, null=True)  # Field name made lowercase.
    groupname = models.TextField(db_column='groupName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    usebaseprice = models.NullBooleanField(db_column='useBasePrice')  # Field name made lowercase.
    allowmanufacture = models.NullBooleanField(db_column='allowManufacture')  # Field name made lowercase.
    allowrecycler = models.NullBooleanField(db_column='allowRecycler')  # Field name made lowercase.
    anchored = models.NullBooleanField()
    anchorable = models.NullBooleanField()
    fittablenonsingleton = models.NullBooleanField(db_column='fittableNonSingleton')  # Field name made lowercase.
    published = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'invGroups'


class Invitems(models.Model):
    itemid = models.BigIntegerField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    typeid = models.BigIntegerField(db_column='typeID')  # Field name made lowercase.
    ownerid = models.BigIntegerField(db_column='ownerID')  # Field name made lowercase.
    locationid = models.BigIntegerField(db_column='locationID')  # Field name made lowercase.
    flagid = models.SmallIntegerField(db_column='flagID')  # Field name made lowercase.
    quantity = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'invItems'


class Invmarketgroups(models.Model):
    marketgroupid = models.BigIntegerField(db_column='marketGroupID', primary_key=True)  # Field name made lowercase.
    parentgroupid = models.BigIntegerField(db_column='parentGroupID', blank=True, null=True)  # Field name made lowercase.
    marketgroupname = models.TextField(db_column='marketGroupName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.
    hastypes = models.NullBooleanField(db_column='hasTypes')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invMarketGroups'


class Invmetagroups(models.Model):
    metagroupid = models.SmallIntegerField(db_column='metaGroupID', primary_key=True)  # Field name made lowercase.
    metagroupname = models.TextField(db_column='metaGroupName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    iconid = models.BigIntegerField(db_column='iconID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invMetaGroups'


class Invmetatypes(models.Model):
    typeid = models.BigIntegerField(db_column='typeID', primary_key=True)  # Field name made lowercase.
    parenttypeid = models.BigIntegerField(db_column='parentTypeID', blank=True, null=True)  # Field name made lowercase.
    metagroupid = models.SmallIntegerField(db_column='metaGroupID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invMetaTypes'


class Invnames(models.Model):
    itemid = models.BigIntegerField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    itemname = models.TextField(db_column='itemName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invNames'


class Invpositions(models.Model):
    itemid = models.BigIntegerField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    yaw = models.FloatField(blank=True, null=True)
    pitch = models.FloatField(blank=True, null=True)
    roll = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invPositions'


class Invtraits(models.Model):
    
    typeid = models.BigIntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    skillid = models.BigIntegerField(db_column='skillID', blank=True, null=True)  # Field name made lowercase.
    bonus = models.FloatField(blank=True, null=True)
    bonustext = models.TextField(db_column='bonusText', blank=True)  # Field name made lowercase.
    unitid = models.BigIntegerField(db_column='unitID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invTraits'


class Invtypematerials(models.Model):
    
    typeid = models.BigIntegerField(db_column='typeID')  # Field name made lowercase.
    materialtypeid = models.BigIntegerField(db_column='materialTypeID')  # Field name made lowercase.
    quantity = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'invTypeMaterials'


class Invtypereactions(models.Model):
    
    reactiontypeid = models.BigIntegerField(db_column='reactionTypeID')  # Field name made lowercase.
    input = models.BooleanField(default=False)
    typeid = models.BigIntegerField(db_column='typeID')  # Field name made lowercase.
    quantity = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invTypeReactions'


class Invtypes(models.Model):
    typeid = models.BigIntegerField(db_column='typeID', primary_key=True)  # Field name made lowercase.
    groupid = models.BigIntegerField(db_column='groupID', blank=True, null=True)  # Field name made lowercase.
    typename = models.TextField(db_column='typeName', blank=True)  # Field name made lowercase.
    description = models.TextField(blank=True)
    mass = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    capacity = models.FloatField(blank=True, null=True)
    portionsize = models.BigIntegerField(db_column='portionSize', blank=True, null=True)  # Field name made lowercase.
    raceid = models.SmallIntegerField(db_column='raceID', blank=True, null=True)  # Field name made lowercase.
    baseprice = models.DecimalField(db_column='basePrice', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    published = models.NullBooleanField()
    marketgroupid = models.BigIntegerField(db_column='marketGroupID', blank=True, null=True)  # Field name made lowercase.
    chanceofduplicating = models.FloatField(db_column='chanceOfDuplicating', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invTypes'


class Invuniquenames(models.Model):
    itemid = models.BigIntegerField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    itemname = models.TextField(db_column='itemName', unique=True)  # Field name made lowercase.
    groupid = models.BigIntegerField(db_column='groupID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invUniqueNames'


class Invvolumes(models.Model):
    groupid = models.BigIntegerField(primary_key=True)
    volume = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invVolumes'
