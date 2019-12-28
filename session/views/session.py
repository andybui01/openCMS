from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from ..models import Session, Athlete
from ..forms import CreateAthleteForm

def index(request, meet_id, session_id):
    ''' Return results of all athletes in a weightclass '''
    session = get_object_or_404(Session, pk=session_id)

    if session.meet.id != meet_id:
        raise Http404("Session not found!")

    athletes_list = session.athlete_set.all()

    context = {
        'session': session,
        'athletes_list': athletes_list
    }

    return render(request, 'session/index.html', context)

def delete(request, meet_id, session_id):
    ''' Delete a session from a meet '''
    user = request.user
    session = get_object_or_404(Session, pk=session_id)
    if user.is_authenticated and session.meet.user == user:
        session.delete()
        return HttpResponseRedirect(reverse('meet:index', args=[meet_id]))
    else:
        raise Http404()

def athlete_add(request, meet_id, session_id):
    ''' Add athlete to session '''
    session = get_object_or_404(Session, pk=session_id)
    user = request.user
    if user.is_authenticated and session.meet.user == user:
        session.athlete_set.create(
            name = request.POST['name'],
            date_of_birth = request.POST['date_of_birth'],
            gender = request.POST['gender'],
            bodyweight = request.POST['bodyweight'],
            affiliation = request.POST['affiliation']
        )
    else:
        raise Http404()

def display_athlete_add(request, meet_id, session_id):
    ''' Render form to create athlete profile '''
    user = request.user

    session = get_object_or_404(Session, pk=session_id)

    if user.is_authenticated and session.meet.user == user:
        form = CreateAthleteForm()
        context = {
            'form':form,
            'session':session
        }

        return render(request, 'session/add_athlete.html', context)
    else:
        raise Http404()