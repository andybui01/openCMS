from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from ..models import Meet

def index(request, meet_id):
    ''' Overview of all ongoing and finished sessions '''
    meet = get_object_or_404(Meet, pk=meet_id)
    
    sessions_list = meet.session_set.all().order_by('start_time')

    context = {
        'meet': meet,
        'sessions_list' : sessions_list
    }

    return render(request, 'meet/index.html', context)

def delete(request, meet_id):
    ''' Delete meet with id: meet_id '''
    
    meet = get_object_or_404(Meet, pk=meet_id)
    meet.delete()

    return HttpResponseRedirect(reverse('homepage:admin'))