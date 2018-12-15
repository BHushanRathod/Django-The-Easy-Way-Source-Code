from django.shortcuts import render

def index(request): # < here
    return render(request, 'myapp/index.html')
