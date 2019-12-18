from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def results(request):
    ''' Return results of all athletes in a weightclass '''
    return HttpResponse("Lol!")

def update(request):
    ''' Update athlete attempts '''
    pass

def create(request):
    ''' Create athlete profile '''
    pass

def delete(request):
    ''' Delete athlete profile '''
    pass
