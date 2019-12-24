from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from ..models import Session, Athlete, Lift

def index(request):
    return HttpResponse("Index page!")

