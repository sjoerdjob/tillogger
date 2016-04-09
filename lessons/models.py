from __future__ import unicode_literals

from django.db import models

from taggit.managers import TaggableManager


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    tags = TaggableManager()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
