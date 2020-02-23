from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from ..models import Session, Athlete
from ..forms import CreateAthleteForm, UpdateAthleteForm

def index(request, meet_id, session_id):
    ''' Return results of all athletes in a weightclass '''
    session = get_object_or_404(Session, pk=session_id)

    if session.meet.id != meet_id:
        raise Http404("Session not found!")

    athletes_list = session.athlete_set.all()

    form = UpdateAthleteForm()

    context = {
        'session': session,
        'athletes_list': athletes_list,
        'form':form
    }

    return render(request, 'session/index.html', context)

def session_delete(request, meet_id, session_id):
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
        athlete = session.athlete_set.create(
            name = request.POST['name'],
            date_of_birth = request.POST['date_of_birth'],
            gender = request.POST['gender'],
            bodyweight = request.POST['bodyweight'],
            affiliation = request.POST['affiliation'].upper()
        )
        athlete.create_lifts()
        return HttpResponseRedirect(reverse('meet:session:index', args=[meet_id,session_id]))
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

def athlete_delete(request, **kwargs):
    ''' Delete athlete from session and meet '''
    user = request.user
    session = get_object_or_404(Session, pk=kwargs['session_id'])

    if user.is_authenticated and session.meet.user == user:
        try:
            athlete = session.athlete_set.get(pk=kwargs['athlete_id'])
            athlete.delete()
        except:
            raise Http404()
        return HttpResponseRedirect(
            reverse(
                'meet:session:manage',
                args=[
                    kwargs['meet_id'],
                    kwargs['session_id']
                ]
            )
        )
    else:
        raise Http404()

def athlete_update(request, **kwargs):
    ''' Update athlete attempt weights '''
    user = request.user
    session = get_object_or_404(Session, pk=kwargs['session_id'])

    if user.is_authenticated and session.meet.user == user:
        # try:
        athlete = session.athlete_set.get(pk=kwargs['athlete_id'])
        athlete.update_attempt(request.POST['attempt'], request.POST['change'], request.POST['weight'])
        athlete.save()
        # except:
        #     raise Http404()
        return HttpResponseRedirect(
            reverse(
                'meet:session:index',
                args=[
                    kwargs['meet_id'],
                    kwargs['session_id']
                ]
            )
        )
    else:
        raise Http404()

def manage(request, meet_id, session_id):
    ''' Return results of all athletes in a weightclass '''
    session = get_object_or_404(Session, pk=session_id)

    if session.meet.id != meet_id:
        raise Http404("Session not found!")

    athletes_list = session.athlete_set.all()

    form = UpdateAthleteForm()

    context = {
        'session': session,
        'athletes_list': athletes_list,
        'form':form
    }

    return render(request, 'session/manage.html', context)
