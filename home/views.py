from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from testimonials.models import Testimonial
from django.core.mail import send_mail
from .models import Project, Service
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm

def home(request):
    services = Service.objects.all()[:3]
    testimonials = Testimonial.objects.filter(is_approved=True)[:5]
    context = {
        'testimonials': testimonials,
        'services': services
    }
    return render(request, 'home/home.html', context)

def projects_page(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'home/projects.html', {'projects': projects})

def services_page(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'home/services.html', context)

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    context = {'service': service}
    return render(request, 'home/service_detail.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Compose the email
            subject = f'New Contact Form Submission from {name}'
            message_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Send the email
            send_mail(
                subject,
                message_body,
                settings.EMAIL_HOST_USER,
                ["shilohe.write@gmail.com"],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Named URL for contact page
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})
