from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name=''),
    path('gallery', views.gallery, name='gallery'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('gallery_single', views.gallery_single, name='gallery-single'),
    path('services', views.services, name='services'),
]