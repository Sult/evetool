from django.db import models



class CallGroup(models.Model):
    """ Groups of different accestypes """

    groupid = models.IntegerField(unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()

    def __unicode__(self):
        return self.name



class Call(models.Model):
    """ integers (for bits) to check for specific access """

    accessmask = models.IntegerField()
    accounttype = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    callgroup = models.ForeignKey(CallGroup)
    description = models.TextField()

    class Meta:
        unique_together = ["accounttype", "name"]
    
    def __unicode__(self):
        return self.name
    
    
