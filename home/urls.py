from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_page, name='projects'),
    path('services/', views.services_page, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('contact/', views.contact_view, name='contact'),
]
