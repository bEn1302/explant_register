from django import template
# Import User Model from Django
from django.contrib.auth.models import User

register = template.Library()

@register.filter
def truncate(value, length):
    # Truncates a string to a certain number of characters, and appends '...' if it was truncated.
    if len(value) > length:
        truncated_value = value[:length].rsplit(' ', 1)[0] + '...'
    else:
        truncated_value = value
    return truncated_value

@register.simple_tag
def get_username_from_id(user_id):
    try:
        user = User.objects.get(pk=user_id)
        return user.username
    except User.DoesNotExist:
        return None