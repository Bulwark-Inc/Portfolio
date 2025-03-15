from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border p-2 w-full'}),
            'email': forms.EmailInput(attrs={'class': 'border p-2 w-full'}),
            'message': forms.Textarea(attrs={'class': 'border p-2 w-full'}),
        }
