from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from ..models import Session, Athlete, Lift

def admin(request):
    ''' Admin page for sessions '''
    
    # Return list of dictionaries
    athletes_list = list(Athlete.objects.all().values())

    context = {
        'athletes_list': athletes_list
    }

    return render(request, 'lifters/admin.html', context)

def clear(request):
    ''' Clear all athletes from database '''

    Athlete.objects.all().delete()

    return HttpResponseRedirect(reverse('lifters:admin'))

def results(request):
    ''' Return results of all athletes in a weightclass '''

    # Return list of dictionaries
    athletes_list = list(Athlete.objects.all().values())

    context = {
        'athletes_list': athletes_list
    }

    return render(request, 'lifters/results.html', context)