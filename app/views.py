from django.shortcuts import render
from .models import image
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request, 'index.html')

def gallery(request):
    images = image.objects.all()
    p = Paginator(image.objects.all(), 1)
    page = request.GET.get('page')
    image_list =p.get_page(page)


    return render(request, 'gallery.html', {'images':images, 'image_list': image_list})

def about(request):
    return render(request, 'about.html')

def gallery_single(request):
    return render(request, 'gallery-single.html')

def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')