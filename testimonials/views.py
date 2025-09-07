from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm

def testimonial_list(request):
    """
    Displays a list of approved testimonials.
    """
    testimonials = Testimonial.objects.filter(is_approved=True).order_by('-date_posted')
    return render(request, 'testimonials/testimonials_list.html', {'testimonials': testimonials})

def submit_testimonial(request):
    """
    Handles the submission of a new testimonial.
    """
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.is_approved = False  # Set to pending approval
            testimonial.save()
            
            # Use f-string for better message formatting
            messages.success(request, f"Thank you, {testimonial.name}! Your testimonial has been submitted and is pending approval.")
            return redirect('testimonials')
        else:
            # Add a message for form errors
            messages.error(request, "There was an error with your submission. Please check the form and try again.")
    else:
        form = TestimonialForm()
    
    return render(request, 'testimonials/submit_testimonial.html', {'form': form})