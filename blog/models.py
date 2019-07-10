from django.db import models
from tinymce.models import HTMLField

class Tag(models.Model):
    tagslug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.tagslug

class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = HTMLField()
    slug = models.SlugField(max_length=200, unique=True)
    published = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
