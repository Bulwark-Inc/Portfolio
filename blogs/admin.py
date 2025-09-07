from django.contrib import admin
from .models import Category, Blog, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('name', 'email', 'message', 'approved', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    can_delete = True


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline]
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'blog', 'approved', 'created_at')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email', 'message')
    actions = ['approve_comments']
    date_hierarchy = 'created_at'

    def approve_comments(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, f"{updated} comment(s) approved.")
    approve_comments.short_description = "Approve selected comments"
