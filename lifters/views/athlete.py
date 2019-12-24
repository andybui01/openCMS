from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from ..models import Session, Athlete, Lift

def details(request, athlete_id):
    ''' Return details of an athlete '''
    athlete = get_object_or_404(Athlete, pk=athlete_id)
    
    context = {
        'athlete': athlete.get_dict()
    }

    return render(request, 'lifters/details.html', context)

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

def remove(request, athlete_id):
    ''' Remove athlete profile '''
    
    athlete = get_object_or_404(Athlete, pk=athlete_id)
    athlete.delete()

    return HttpResponseRedirect(reverse('lifters:admin'))

def update(request, athlete_id):
    ''' Update athlete attempts '''
    pass
