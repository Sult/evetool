from django.db import models
from django.core.cache import cache
from picklefield.fields import PickledObjectField

import utils


class Task(models.Model):
    """
    Task parent. Task will be sometimes generated to run asynchroon
    A worker will run these task one by one when enough resources are free
    """

    VERY_LOW = 0
    LOW = 1
    NORMAL = 2
    HIGH = 3
    VERY_HIGH = 4
    PRIORITIES = (
        #bulk data updates
        (VERY_LOW, "Very Low"),

        (LOW, "Low"),
        #startup some cache user has not visited yet
        (NORMAL, "Normal"),
        #user requests that need to update cache
        (HIGH, "High"),
        #user requests that have no cache yet
        (VERY_HIGH, "Very High"),
    )

    active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(choices=PRIORITIES)

    class Meta:
        abstract = True
        ordering = ["-date"]


class EveApiCache(Task):
    """
    set cache task. Creating new caches, and updating old ones.
    """

    ACCOUNT = "account"
    CHAR = "char"
    CORP = "corp"
    EVE = "eve"
    MAP = "map"
    SERVER = "server"
    API = "API"
    CATEGORIES = (
        (ACCOUNT, "Account"),
        (CHAR, "Char"),
        (CORP, "Corp"),
        (EVE, "Eve"),
        (MAP, "Map"),
        (SERVER, "Server"),
        (API, "API"),
    )

    api = models.ForeignKey('apies.Api', null=True)
    #auth = models.BooleanField(default=True)
    kwargs = PickledObjectField(null=True, blank=True)
    category = models.CharField(max_length=15, choices=CATEGORIES)
    key = models.CharField(max_length=254)
    #cache_key = models.CharField(max_length=254)

    def __unicode__(self):
        return "%s/%s" % (self.category, self.key)

    def cache_key(self):
        return utils.connection.generate_cache_key(
            self.category, self.key, api=self.api, **self.kwargs
        )

    def set_cache(self):
        data = self.request_call()
        #defautl cachetimer is 6 hours
        cache_timer = 60 * 60 * 6
        cache.set(self.cache_key(), data, cache_timer)

    # Get the first part of the api object.
    # it will establish an authenticated connection if needed.
    # the connection will already have the first part of the API uri
    # example uri part: https://api.eveonline.com/Eve/KEY
    # Where KEY will be added before retrieving the information
    # for more information look at https://neweden-dev.com/API
    def connection(self):
        if self.api:
            api = utils.connection.auth_connect(self.api)
        else:
            api = utils.connection.api_connect()
        #return eveapi object
        return getattr(api, self.category)

    # uses connection to retrieve data from specific API key
    # Kwargs should contain all required and/or optional fields
    # so example kwargs for a WalletJournal key with 2500 rows would be
    # self.kwargs = {"characterID": some_character_id, "rowCount": 2500}
    def request_call(self):
        connection = self.connection()
        if self.kwargs:
            return getattr(connection, self.key)(**self.kwargs)
        else:
            return getattr(connection, self.key)()
