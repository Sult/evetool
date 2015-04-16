from django.db import models


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
