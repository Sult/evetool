from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """
    Unlocking options for leadership. Also used for settings like
    access, contact information and more
    """

    FREE = 0
    SILVER = 1
    GOLD = 2
    PLATINUM = 3
    MEMBERSHIPS = (
        (FREE, "Free"),
        (SILVER, "Silver"),
        (GOLD, "Gold"),
        (PLATINUM, "Platinum"),
    )

    CORPORATION = 0
    ALLIANCE = 1
    COALITION = 2
    CATEGORIES = (
        (CORPORATION, "Corporation"),
        (ALLIANCE, "Alliance"),
        (COALITION, "Coalition"),
    )

    ceo = models.ForeignKey(User)
    category = models.IntegerField(choices=CATEGORIES)
    membership = models.IntegerField(choices=MEMBERSHIPS, default=FREE)
    created = models.DateField(auto_now_add=True)
    paid_until = models.DateField(null=True)
    email = models.EmailField(max_length=254)

    name = models.CharField(max_length=254, unique=True)
    key = models.BigIntegerField(null=True)

    def __unicode__(self):
        return "%s: %s" % (self.ceo.username, self.name)


class Leadership(models.Model):
    """ appointed directors that should have acces to the account pannel """

    account = models.ForeignKey("users.Account")
    director = models.ForeignKey(User)

    class Meta:
        unique_together = ["account", "director"]

    def __unicode__(self):
        return "%s: %s" % (self.account.name, self.director.username)
