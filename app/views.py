from django.shortcuts import render
from .models import image
# Create your views here.

def index(request):
    return render(request, 'index.html')

def gallery(request):
    images = image.objects.all
    return render(request, 'gallery.html', {'images':images})

def about(request):
    return render(request, 'about.html')

def gallery_single(request):
    return render(request, 'gallery-single.html')

def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')