from django.contrib import admin

from rpg.models import Entity, Story
admin.site.register(Entity)
admin.site.register(Story)
admin.site.site_header = "First Studio.co"
