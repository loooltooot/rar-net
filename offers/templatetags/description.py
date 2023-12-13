from django import template

register = template.Library()

@register.simple_tag
def description(text):
    return text[:70] + '...' if len(text) > 70 else text