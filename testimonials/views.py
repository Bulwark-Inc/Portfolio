from django.shortcuts import render, redirect
from .models import Testimonial
from .forms import TestimonialForm
from django.contrib import messages

def testimonial_list(request):
    testimonials = Testimonial.objects.filter(is_approved=True).order_by('-date_posted')
    return render(request, 'testimonials/testimonials_list.html', {'testimonials': testimonials})


def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.is_approved = False  # Require admin approval
            testimonial.save()
            messages.success(request, "Thank you! Your testimonial has been submitted and is pending approval.")
            return redirect('testimonials')  # or wherever you want to send them
    else:
        form = TestimonialForm()
    
    return render(request, 'testimonials/submit_testimonial.html', {'form': form})