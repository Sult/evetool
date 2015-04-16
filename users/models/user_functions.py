from datetime import timedelta, datetime
from collections import OrderedDict

from django.utils import timezone
from django.contrib.auth.models import User


#return list of inactive users
@staticmethod
def inactive_dict():
    users = User.objects.order_by("username")
    temp = OrderedDict()
    for user in users:
        if user.is_inactive():
            temp[user.username] = user.days_since_last_login()
    return temp


#see when user is inactive
def is_inactive(self):
    now = datetime.utcnow().replace(tzinfo=timezone.utc) + timedelta(days=30)
    if now > self.last_login.replace(tzinfo=timezone.utc):
        return False
    else:
        return True


#see how long ago a user last logged in
def days_since_last_login(self):
    now = datetime.utcnow().replace(tzinfo=timezone.utc)
    delta = now - self.last_login.replace(tzinfo=timezone.utc)
    if delta.days == 0:
        return "Today"
    else:
        return "%d days ago" % delta.days


User.add_to_class("is_inactive", is_inactive)
User.add_to_class("days_since_last_login", days_since_last_login)
User.add_to_class("inactive_dict", inactive_dict)

