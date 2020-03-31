from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def h1(value):
    return mark_safe(f'<h1>{value}</h1>')


register.simple_tag(h1, name='h1')
