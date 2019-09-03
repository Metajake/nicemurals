from django.db import models

from ckeditor.fields import RichTextField

from portfolio.models import Work, Project, Portrait

class Tag(models.Model):
    tagslug = models.SlugField(max_length=200, unique=True)
    summary = models.CharField(max_length = 200)

    def __str__(self):
        return self.tagslug

class Entry(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    weapon_type = models.CharField(max_length=30, choices=[('summary', 'summary'),('summary_large_image','summary_large_image')], default='summary')
    is_published = models.BooleanField(default = True)
    richbody = RichTextField(blank=True)
    description = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Tag, blank=True, on_delete=models.CASCADE, null=True)
    tweet_version = models.IntegerField(editable=False, default=0)
    featured_image = models.OneToOneField(Work, related_name="entry_featured_image", on_delete= models.CASCADE, blank=True, null=True)
    images = models.ManyToManyField(Work, related_name="entry_images", blank=True)
    fire_laser = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

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
        verbose_name_plural = "Journal"

class History(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    story = RichTextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "History"

class Affiliate(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ImageField(upload_to='uploads/blog/')
    enabled = models.BooleanField(default=True)
    link = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class Config(models.Model):
    entry_sorting = models.CharField(max_length=100, choices=[('tiles','tiles'),('columns','columns')], default="columns")
    rpg_active = models.BooleanField(default=False)
    in_location = models.BooleanField(default=False)
    in_space = models.BooleanField(default=False)
    language = models.CharField(max_length=10, choices=[('ja','Japanese'),('en','English'),('es','Espanol'),('fr','French'),('de','German'),('sv','Swedish'),('zh','Chinese')], default='ja')
    author_description = RichTextField(blank=True)
    profile_picture = models.ForeignKey(Portrait, related_name="profile_picture", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "Blog Config"

    class Meta:
        verbose_name_plural = "Configuration"
