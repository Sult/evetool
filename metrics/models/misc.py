from django.db import models


class Sovereignty(models.Model):
    """ what solarsystems can change owners """

    solarsystemid = models.BigIntegerField(unique=True)
    solarsystemname = models.CharField(max_length=254, unique=True)

    def __unicode__(self):
        return self.solarsystemname


class SovereigntyHolder(models.Model):
    """ who holds the sovereignty of a system """

    sovereignty = models.ForeignKey("metrics.Sovereignty")
    allianceid = models.BigIntegerField(null=True)
    corporationid = models.BigIntegerField(null=True)
    factionid = models.BigIntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.sovereignty.solarsystemname
