from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from ..models import Session, Athlete

def index(request, meet_id, session_id):
    ''' Return results of all athletes in a weightclass '''
    session = get_object_or_404(Session, pk=session_id)

    if session.meet.id != meet_id:
        raise Http404("Session not found!")

    athletes_list = session.athlete_set.all()

    context = {
        'session_name': str(session),
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