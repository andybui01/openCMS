from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from ..forms import MeetForm


def index(request):
    ''' Landing page for openCMS '''
    form = MeetForm()
    return render(request, 'homepage/index.html', {'form': form})
    
def redirect_meet(request):
    ''' Redirect to meet page specified by meet_id '''
    meet_id = request.GET['meet_id']
    return HttpResponseRedirect(reverse('meet:index', args=(meet_id)))

def test(request):
    meet_id = request.GET['meet_id']
    print(meet_id)
    return HttpResponse("Works!")