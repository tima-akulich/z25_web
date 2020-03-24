from django import template


register = template.Library()


def reverse_str(value, param):
    return value[:param:-1]


def my_tag(parser, token):
    return f'{parser} {token}'


register.filter('reverse_str', reverse_str)

register.tag('my_tag', my_tag)
