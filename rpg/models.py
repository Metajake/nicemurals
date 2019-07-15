from django.db import models

class Entity(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
