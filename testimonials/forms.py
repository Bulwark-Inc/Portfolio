from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'designation', 'message', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Your Name'}),
            'designation': forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Your Title/Role'}),
            'message': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'Your Testimonial'}),
            'photo': forms.FileInput(attrs={'class': 'border p-2 w-full'}),
        }
