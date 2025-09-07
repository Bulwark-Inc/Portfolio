from django.contrib import admin
from .models import Project, Service, DailyHeroText
from django.utils import timezone
from django.db.models import F

@admin.register(DailyHeroText)
class DailyHeroTextAdmin(admin.ModelAdmin):
    list_display = ('header', 'last_displayed', 'is_active')
    list_filter = ('is_active', 'last_displayed')
    search_fields = ('header', 'body')
    readonly_fields = ('last_displayed',)
    list_editable = ('is_active',)
    date_hierarchy = 'last_displayed'

    def display_now_action(self, request, queryset):
        """Action to immediately display the selected text on the homepage."""
        queryset.update(last_displayed=timezone.now().date())
        self.message_user(request, "Selected text has been marked for immediate display.")
    display_now_action.short_description = "Mark for immediate display"

    actions = [display_now_action]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'live_demo_link')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}