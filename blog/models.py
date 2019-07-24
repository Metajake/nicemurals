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
    featured_image = models.OneToOneField(Work, related_name="entry_featured_image", on_delete= models.CASCADE, blank=True, null=True)
    images = models.ManyToManyField(Work, related_name="entry_images", blank=True)
    fire_laser = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"

class Journal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    weather = models.CharField(max_length=100)
    plan = models.CharField(max_length=200)
    what_you_did = RichTextField(blank=True)

    def __str__(self):
        return self.created.strftime('%Y-%m-%d')
        
    class Meta:
        verbose_name_plural = "Journal Entries"

class Config(models.Model):
    entry_sorting = models.CharField(max_length=100, choices=[('tiles','tiles'),('columns','columns')], default="columns")
    rpg_active = models.BooleanField(default=False)
