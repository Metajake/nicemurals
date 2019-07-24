from django.contrib import admin

from .models import Work, Project, Category

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ('title',),
    }

admin.site.register(Work)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
