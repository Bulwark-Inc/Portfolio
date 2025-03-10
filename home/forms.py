from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        subject = f'Portfolio Contact from {self.cleaned_data["name"]}'
        message = self.cleaned_data['message']
        from_email = self.cleaned_data['email']
        recipient_list = [settings.EMAIL_HOST_USER]

        send_mail(subject, message, from_email, recipient_list)
