from django.urls import path, include
from .views import meet

app_name='meet'

urlpatterns = [
    path('', meet.index, name='index'),
    path('<int:session_id>/', include('session.urls', namespace='session')),
    path('add-session-form/', meet.display_add_form, name="display_add_form"),
    path('add-session/', meet.session_add, name="session_add"),
    path('delete-meet/', meet.meet_delete, name="meet_delete"),
]