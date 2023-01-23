from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage':'Hello World!!!'}
    return render(request, 'Rango/index.html', context=context_dict)


def about(request):
    return HttpResponse("'Rango says here is the about page.")