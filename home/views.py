from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm
from django.contrib import messages

def home(request):
    return render(request, 'home/home.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'home/projects.html', {'projects': projects})

def services(request):
    return render(request, 'home/services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            messages.success(request, 'Message sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})
