from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def russel(request):
    return HttpResponse('<h1> Welcome Russel </h1>')