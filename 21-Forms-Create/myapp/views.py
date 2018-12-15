from django.shortcuts import render
from myapp.models import Flower
from django.http import HttpResponseRedirect
from .forms import MyForm

def index(request):

    flowers = Flower.objects.all()
    
    return render(request, 'myapp/index.html', {'flowers': flowers })

def create(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    return render(request, 'myapp/edit.html', {'form': form})
