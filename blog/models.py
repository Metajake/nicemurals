from django.db import models

from ckeditor.fields import RichTextField

from portfolio.models import Work

class Tag(models.Model):
    tagslug = models.SlugField(max_length=200, unique=True)
    summary = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.tagslug

class Entry(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    weapon_type = models.CharField(max_length=30, choices=[('summary', 'summary'),('summary_large_image','summary_large_image')], default='summary')
    published = models.BooleanField(default = True)
    richbody = RichTextField(blank=True)
    description = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    tweet_version = models.IntegerField(editable=False, default=0)
    images = models.ManyToManyField(Work, blank=True)
    fire_laser = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Config(models.Model):
    card_sorting = models.CharField(max_length=100, choices=[('tiles','tiles'),('columns','columns')], default="columns")
    rpg_active = models.BooleanField(default=False)
