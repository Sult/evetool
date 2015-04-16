from datetime import datetime, timedelta

from django.conf import settings
from django.utils.timezone import utc


#converts a timestamp to a aware datetime object
def convert_timestamp(timestamp):
    try:
        temp = datetime.fromtimestamp(timestamp).replace(tzinfo=utc)
        return temp
    except TypeError:
        return None


#see if you reached last iteration of a forloop
def lookahead(iterable):
    it = iter(iterable)
    last = it.next()
    for val in it:
        yield last, False
        last = val
    yield last, True


##### ICONS #####
#Get the size name of an icon
def icon_size_name(size):
    for s in settings.IMAGE_SIZES:
        if s[1] == size:
            return s[0]


#get the last restart datetime for eve server
def last_server_restart():
    now = datetime.now().replace(tzinfo=utc)
    if now.hour < 12:
        now = now - timedelta(days=1)
    restart = now.replace(hour=12, minute=0, second=0, microsecond=0)
    return restart
