from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'border border-gray-300 p-2 w-full rounded',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'border border-gray-300 p-2 w-full rounded',
        'placeholder': 'Your Email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'border border-gray-300 p-2 w-full rounded',
        'placeholder': 'Your Message'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'border border-gray-300 p-2 w-full rounded',
        'placeholder': 'Your Message'
    }))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(attrs={
        'class': 'border border-gray-300 p-2 w-full rounded'
    }))