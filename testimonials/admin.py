from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'is_approved', 'date_posted')
    list_filter = ('is_approved', 'date_posted')
    search_fields = ('name', 'designation', 'message')
