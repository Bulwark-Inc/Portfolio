from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonial_list, name='testimonials'),
    path('submit/', views.submit_testimonial, name='submit_testimonial'),
]
