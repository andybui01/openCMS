from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from lifters.models import Athlete, Lift

def results(request):
    ''' Return results of all athletes in a weightclass '''
    lifter = get_object_or_404(Athlete, pk=1)

    return HttpResponse(str(lifter))

def update(request):
    ''' Update athlete attempts '''
    pass

def create(request):
    ''' Create athlete profile '''
    pass

def delete(request):
    ''' Delete athlete profile '''
    pass
