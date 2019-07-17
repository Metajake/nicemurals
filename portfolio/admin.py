from django.contrib import admin

from .models import Work, Project

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ('project_name',),
    }

admin.site.register(Work)
admin.site.register(Project, ProjectAdmin)
