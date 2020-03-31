from django import template

register = template.Library()


def reverse_str(value, param):
    return value[:param:-1]


register.filter('reverse_str', reverse_str)
