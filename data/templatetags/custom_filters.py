from django import template
from django.utils.html import strip_tags

register = template.Library()

@register.filter
def truncate(value, length):
    # Truncates a string to a certain number of characters, and appends '...' if it was truncated.
    if len(value) > length:
        truncated_value = value[:length].rsplit(' ', 1)[0] + '...'
    else:
        truncated_value = value
    return truncated_value