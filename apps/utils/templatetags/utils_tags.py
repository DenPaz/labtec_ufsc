from django import template
from django.urls import NoReverseMatch, reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def is_active(context, *args, **kwargs):
    request_path = context.get("request").path
    for url_name in args:
        try:
            if request_path == reverse(url_name):
                return "active"
        except NoReverseMatch:
            pass
    return ""
