from datetime import datetime

from django.db import models
from django.utils.timezone import utc


class Character(models.Model):
    """ character within eve """

    lastrefresh = models.DateTimeField(null=True)
    characterid = models.BigIntegerField(unique=True)
    charactername = models.CharField(max_length=254, unique=True)
    corporationid = models.BigIntegerField()
    corporationname = models.CharField(max_length=254, blank=True)
    corporationdate = models.DateTimeField(null=True)
    allianceid = models.BigIntegerField(null=True)
    alliancedate = models.DateTimeField(null=True)
    securitystatus = models.FloatField(default=0.0)

    def __unicode__(self):
        return self.charactername

    #refresh the timer while saving object
    def save(self, *args, **kwargs):
        now = datetime.now().replace(tzinfo=utc)
        self.lastrefresh = now
        super(Character, self).save(*args, **kwargs)


# class EmploymentHistory(models.Model):
#     """ all previous corporations of a character """

#     characterid = models.BigIntegerField()
#     corporationid = models.BigIntegerField()
#     startdate = models.DateTimeField()

#     class Meta:
#         unique_together = ["characterid", "startdate"]
