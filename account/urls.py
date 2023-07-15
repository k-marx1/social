from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views

urlpatterns = [

    # Login urls
    path('', include('django.contrib.auth.urls')),

    # Dashboard url
    path('', views.dashboard, name='dashboard'),

    # Register url
    path('register/', views.register, name='register'),

    # Edit user's & profile's data url
    path('edit/', views.edit, name='edit'),


]

# Remove section below on production
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
