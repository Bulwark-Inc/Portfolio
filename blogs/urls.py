from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blogs'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),  # Single post
]
