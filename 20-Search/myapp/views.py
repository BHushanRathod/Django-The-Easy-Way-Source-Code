from django.shortcuts import render

from myapp.models import Flower

def index(request):

    q = request.GET.get('q', None)
    flowers = ''
    if q is None or q is "":
        flowers = Flower.objects.all()
    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)
    
    return render(request, 'myapp/index.html', {'flowers': flowers })
