from django.db import models

from ckeditor.fields import RichTextField

from portfolio.models import Work

class Tag(models.Model):
    tagslug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.tagslug

class Entry(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    published = models.BooleanField(default = True)
    richbody = RichTextField(blank=True)
    description = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    tweet_version = models.IntegerField(editable=False, default=0)
    images = models.ManyToManyField(Work, blank=True)

    def __str__(self):
        return self.title
