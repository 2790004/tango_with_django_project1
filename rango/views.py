from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context_dict = {'boldmessage':'Hello World!!!'}
    return render(request, 'Rango/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage':'Hello World!!!'}
    return render(request, 'Rango/about.html', context=context_dict)