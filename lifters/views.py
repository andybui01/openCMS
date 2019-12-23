from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Athlete, Lift


def admin(request):
    ''' Admin page for meets '''
    
    # Return list of dictionaries
    athletes_list = list(Athlete.objects.all().values())

    context = {
        'athletes_list': athletes_list
    }


    return render(request, 'lifters/admin.html', context)

def results(request):
    ''' Return results of all athletes in a weightclass '''

    # Return list of dictionaries
    athletes_list = list(Athlete.objects.all().values())

    context = {
        'athletes_list': athletes_list
    }

    return render(request, 'lifters/index.html', context)

def update(request):
    ''' Update athlete attempts '''
    pass

def create(request):
    ''' Create athlete profile '''

    new_athlete = Athlete(
        name = request.POST['name'],
        date_of_birth = request.POST['date_of_birth'],
        gender = True if request.POST['gender'] == "Male" else False,
        bodyweight = request.POST['bodyweight'],
        affiliation = request.POST['affiliation'].upper()
    )

    new_athlete.save()

    return HttpResponseRedirect(reverse('lifters:admin'))

def delete(request):
    ''' Delete athlete profile '''
    pass
