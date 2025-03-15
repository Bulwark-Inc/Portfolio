# home/admin.py
from django.contrib import admin
from .models import Project, Service

admin.site.register(Service)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description')

