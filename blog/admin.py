from django.contrib import admin

from .models import Entry, Tag, Config, Journal, History

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug" : ("title",),
    }
admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
admin.site.register(Config)
admin.site.register(Journal)
admin.site.register(History)
