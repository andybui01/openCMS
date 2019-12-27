from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from ..forms import MeetForm


def index(request):
    ''' Landing page for openCMS '''
    form = MeetForm()
    return render(request, 'homepage/index.html', {'form': form})
    
def add(request):
    ''' Create meet and associate with user '''
    current_user = request.user

    if current_user.is_authenticated:
        current_user.meet_set.create(name=request.POST['name'])
        return HttpResponseRedirect(reverse('homepage:admin'))
    else:
        return Http404()

def admin(request):
    ''' Admin page for users to manage their meets '''
    current_user = request.user

    if current_user.is_authenticated:
        meet_list = current_user.meet_set.all()
        context = {
            'meet_list':meet_list
        }
        return render(request, 'homepage/admin.html', context)
    else:
        return HttpResponseRedirect(reverse('homepage:login'))

def redirect_meet(request):
    ''' Redirect to meet page specified by meet_id '''
    meet_id = request.GET['meet_id']
    return HttpResponseRedirect(reverse('meet:index', args=(meet_id)))

def test(request):
    meet_id = request.GET['meet_id']
    print(meet_id)
    return HttpResponse("Works!")