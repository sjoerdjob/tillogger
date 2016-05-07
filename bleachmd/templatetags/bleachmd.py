from __future__ import unicode_literals

from django import template
from django.utils.html import mark_safe

import markdown
import markdown.extensions.headerid  # Needs force-importing.
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
def bleachmd_title(value):
    return mark_safe(bleach.clean(
        markdown.markdown(
            '# {}'.format(value),
            [markdown.extensions.headerid.HeaderIdExtension(level=2)],
        ),
        tags=ALLOWED_TAGS,
    ))


@register.filter
def bleachmd(value):
    return mark_safe(bleach.clean(
        markdown.markdown(
            value,
            [markdown.extensions.headerid.HeaderIdExtension(level=3)],
        ),
        tags=ALLOWED_TAGS,
    ))
