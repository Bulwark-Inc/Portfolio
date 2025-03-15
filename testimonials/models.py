from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True, help_text="E.g. CEO, Freelancer")
    message = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return f"{self.name} - {self.designation}"
