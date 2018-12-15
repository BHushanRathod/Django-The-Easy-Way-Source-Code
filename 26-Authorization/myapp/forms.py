from django import forms
from django.forms import ModelForm
from .models import Flower

class MyForm(ModelForm):
    title = forms.CharField(label='Title', 
        widget = forms.TextInput(attrs={'class': 'form-control '})) 
    description = forms.CharField(label='Description',
        widget = forms.Textarea(attrs={'class': 'form-control '})) 
    class Meta:
        model = Flower
        fields = ['title', 'description']
