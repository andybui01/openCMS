from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from ..models import Meet
from ..forms import SessionForm

def index(request, meet_id):
    ''' Overview of all ongoing and finished sessions '''
    meet = get_object_or_404(Meet, pk=meet_id)
    
    sessions_list = meet.session_set.all().order_by('start_time')

    context = {
        'meet': meet,
        'sessions_list' : sessions_list
    }

    return render(request, 'meet/index.html', context)

def add(request, meet_id):
    ''' Add session to meet specified by meet_id '''
    meet = get_object_or_404(Meet, pk=meet_id)
    meet.session_set.create(
        bodyweight=request.POST['bodyweight'],
        letter=request.POST['letter'].upper(),
        start_time=request.POST['start_time']
    )
    return HttpResponseRedirect(reverse('meet:index', args=[meet_id]))

def delete(request, meet_id):
    ''' Delete meet with id: meet_id '''
    
    meet = get_object_or_404(Meet, pk=meet_id)
    meet.delete()

    return HttpResponseRedirect(reverse('homepage:admin'))

def display_add_form(request, meet_id):
    ''' View to render form to create a session '''
    current_user = request.user

    meet = get_object_or_404(Meet, pk=meet_id)

    if current_user.is_authenticated and meet.user == current_user:
        form = SessionForm()
        context = {
            'form':form,
            'meet':meet
        }

        return render(request, 'meet/add_session.html', context)
    elif current_user.is_authenticated:
        return HttpResponseRedirect(reverse('meet:index'))
    else:
        return HttpResponseRedirect(reverse('homepage:index'))