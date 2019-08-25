from django.db import models

from ckeditor.fields import RichTextField

class Category(models.Model):
    category_slug = models.SlugField(max_length=200, unique=True)
    summary = models.CharField(max_length = 200, blank=True)

    def __str__(self):
        return self.category_slug

    class Meta:
        verbose_name_plural = "Categories"

class Tag(models.Model):
    tag_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.tag_name

class Work(models.Model):
    title = models.CharField(max_length=300, blank=True)
    caption = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to="uploads/portfolio/")
    rating = models.CharField(max_length=20, choices=(('pg','PG'),('pg13','PG-13'),('r','R')))
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Portrait(models.Model):
    title = models.CharField(max_length=300, blank=True)
    caption = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to="uploads/portraits/")
    rating = models.CharField(max_length=20, choices=(('pg','PG'),('pg13','PG-13'),('r','R')))
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    is_published = models.BooleanField(default=True)
    description = RichTextField(blank=True)
    featured_image = models.ForeignKey(Work, related_name="project_featured_image", on_delete=models.CASCADE, blank=True, null=True)
    images = models.ManyToManyField(Work, related_name="project_images", blank=True)
    repository = models.CharField(max_length=300, blank=True)
    affiliate_links = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)

    def __str__(self):
        return self.title
