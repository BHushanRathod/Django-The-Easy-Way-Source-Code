from django.shortcuts import render

from myapp.models import Flower

def index(request):

    flowers = Flower.objects.all()
    
    return render(request, 'myapp/index.html', {'flowers': flowers })

def tags(request, slug=None):

    flowers = Flower.objects.filter(tags__slug=slug)
    
    return render(request, 'myapp/index.html', {'flowers': flowers })
