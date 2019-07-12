from django.db import models
from ckeditor.fields import RichTextField

class Tag(models.Model):
    tagslug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.tagslug

class Entry(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    published = models.BooleanField(default = True)
    richbody = RichTextField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    tweet_version = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.title
