from __future__ import unicode_literals

from django import template
from django.utils.html import mark_safe

import markdown
import bleach

register = template.Library()

ALLOWED_TAGS = [
    'code',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'li',
    'p',
    'pre',
    'ul',
]


@register.filter
def bleachmd(value):
    return mark_safe(bleach.clean(
        markdown.markdown(value),
        tags=ALLOWED_TAGS,
    ))
