from django.db import models

class Work(models.Model):
    title = models.CharField(max_length=300, blank=True)
    caption = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to="uploads/portfolio/")
    rating = models.CharField(max_length=20, choices=(('pg','PG'),('pg13','PG-13'),('r','R')))
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title
