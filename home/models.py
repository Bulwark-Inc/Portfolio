from django.db import models

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
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)  # optional: for icon classes
    link = models.URLField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title[:3][:])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
