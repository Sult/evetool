from datetime import datetime, timedelta

from django import template
from django.utils.timezone import utc

from apps.characters.models import CharacterApi
from apps.characters.models import Skill, RefType

from utils.common import convert_timestamp

register = template.Library()


@register.filter
def training_time(timestamp):
    date = convert_timestamp(timestamp)
    if date:
        return date
    else:
        return "Not in training"


@register.filter
def convert_stamp(timestamp):
    return convert_timestamp(timestamp)


@register.filter
def station_name(stationID):
    try:
        station = CharacterApi.find_station(stationID)
        name = station.stationName
        return name
    except AttributeError:
        return "Unknown"


@register.filter
def paid_until(timestamp):
    date = convert_timestamp(timestamp)
    now = datetime.now().replace(tzinfo=utc)
    if now < date:
        return date
    else:
        return "Inactive"


@register.filter
def remap_available(timestamp):
    last = convert_timestamp(timestamp)
    now = datetime.now()
    try:
        remap = last + timedelta(days=365)
    except TypeError:
        return "Error"

    if remap > now:
        return "Now available!"
    else:
        return remap


@register.filter
def skill_name(typeid):
    skill = Skill.objects.get(typeid=typeid)
    return skill.typename


@register.filter
def skill_pk(typeid):
    skill = Skill.objects.get(typeid=typeid)
    return skill.pk


@register.filter
def total_skillpoints(group, group_dict):
    return group_dict[group]


@register.filter
def jump_fatigue(seconds):
    return datetime.now() + timedelta(seconds=seconds)


@register.filter
def reftypename(reftypeid):
    try:
        name = RefType.objects.get(reftypeid=reftypeid).reftypename
        return name
    except RefType.DoesNotExist:
        return "Unknown"
