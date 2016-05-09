from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from taggit.managers import TaggableManager


@python_2_unicode_compatible
class Lesson(models.Model):
    class Meta:
        ordering = ('-modified_at',)

    title = models.CharField(max_length=255)
    tags = TaggableManager()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
