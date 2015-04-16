from django.db import models


class RefType(models.Model):
    """ references for wallet transactions """

    reftypeid = models.IntegerField(unique=True)
    reftypename = models.CharField(max_length=254)

    def __unicode__(self):
        return self.reftypename
