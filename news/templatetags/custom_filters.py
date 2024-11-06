from django import template
from datetime import datetime

register = template.Library()

@register.filter
def format_datetime(value):
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return dt.strftime("%B %d, %Y, %I:%M %p")
    except (ValueError, TypeError):
        return value  
