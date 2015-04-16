from django import template
from django.core.urlresolvers import reverse

register = template.Library()


#TODO: make this work for dynamic urls as well
@register.filter
def find_url(name):
    return reverse(name)
