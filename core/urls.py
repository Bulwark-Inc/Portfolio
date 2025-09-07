from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/s12/admin', admin.site.urls),
    path('', include('home.urls')),
    path('blogs/', include('blogs.urls')),
    path('testimonials/', include('testimonials.urls')),
    path('chatbot/', include('chatbot.urls')),
] 

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)