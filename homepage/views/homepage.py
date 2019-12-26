from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    ''' Landing page for openCMS '''
    return HttpResponse("Index page for our site!")