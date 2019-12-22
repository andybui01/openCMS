from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Athlete, Lift


def admin(request):
    ''' Admin page for meets '''
    
    return render(request, 'lifters/admin.html')

def results(request):
    ''' Return results of all athletes in a weightclass '''

    # Return list of dictionaries
    lifters_list = list(Athlete.objects.all().values())

    context = {
        'lifters_list': lifters_list
    }

    return render(request, 'lifters/index.html', context)

def update(request):
    ''' Update athlete attempts '''
    pass

def create(request):
    ''' Create athlete profile '''
    return HttpResponse("This works!")

def delete(request):
    ''' Delete athlete profile '''
    pass
