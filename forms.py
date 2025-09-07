from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Your email'}),
            'message': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Your message', 'rows': 4}),
        }