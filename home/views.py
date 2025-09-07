from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
from .models import DailyHeroText, Project, Service
from testimonials.models import Testimonial
from utils.email_utils import send_custom_email
from datetime import datetime, date
import random


def home(request):
    """Landing page view: shows featured services and approved testimonials."""
    services = Service.objects.all()[:3]
    testimonials = Testimonial.objects.filter(is_approved=True)[:5]
    current_time = datetime.now()
    today = date.today()

    # Get all entries that have not been displayed today
    candidates = list(DailyHeroText.objects.filter(is_active=True, last_displayed__lt=today).order_by('?'))
    if candidates:
        daily_text = random.choice(candidates)
        daily_text.last_displayed = today
        daily_text.save()
    else:
        daily_text = DailyHeroText.objects.filter(is_active=True).order_by('?').first()

    context = {
        'now': current_time,
        'testimonials': testimonials,
        'services': services,
        'daily_text': daily_text,
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
    other_services = Service.objects.all().exclude(slug=slug)
    
    context = {
        'service': service,
        'other_services': other_services
    }
    return render(request, 'home/service_detail.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            context = {'name': name, 'email': email, 'message': message}

            # 1. Email to admin
            send_custom_email(
                subject=f'New Contact Form Submission from {name}',
                template_name='emails/contact_to_admin.html',
                context=context,
                recipient_list=['shilohe.write@gmail.com'],
            )

            # 2. Confirmation email to sender
            send_custom_email(
                subject='Thank You for Contacting Us!',
                template_name='emails/contact_to_sender.html',
                context=context,
                recipient_list=[email],
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})