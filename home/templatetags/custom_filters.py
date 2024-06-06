from django import template

register = template.Library()
@register.filter
def multiply(value, arg):
    return value * arg


register = template.Library()
@register.filter
def times(number):
    if number is None:
        number = 0
    return range(number)
