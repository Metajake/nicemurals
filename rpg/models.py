from django.db import models

from ckeditor.fields import RichTextField

class Entity(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Entities"

class Story(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=20, choices=(('pg','PG'),('pg13','PG-13'),('r','R')))
    body = RichTextField()

    def __str__(self):
        return self.title
