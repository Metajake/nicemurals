from django.contrib import admin

from .models import Entry, Tag, Config

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug" : ("title",),
    }
admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
admin.site.register(Config)
