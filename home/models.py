from django.db import models
from django.utils import timezone
from django.db.models import F

class Project(models.Model):
    CATEGORY_CHOICES = (
        ('web', 'Web Development'),
        ('mobile', 'Mobile Development'),
        ('ai', 'AI / Machine Learning'),
        ('other', 'Other'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True, null=True)
    live_demo_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class DailyHeroText(models.Model):
    header = models.CharField(max_length=150)
    body = models.TextField()
    is_active = models.BooleanField(default=True)
    last_displayed = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Daily Text: {self.header[:20]}..."