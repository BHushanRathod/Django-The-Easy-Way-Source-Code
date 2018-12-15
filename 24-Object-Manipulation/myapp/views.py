from django.shortcuts import render, get_object_or_404
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

def edit(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == "POST":
        form = MyForm(request.POST, instance=flower)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm(instance=flower)
        
    return render(request, 'myapp/edit.html', {'form': form})

def delete(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    flower.delete()
        
    return render(request, 'myapp/index.html')
