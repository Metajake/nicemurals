from django.db import models
from tinymce.models import HTMLField

class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = HTMLField()

    def __str__(self):
        return self.title
