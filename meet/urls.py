from django.urls import path, include
from .views import meet

app_name='meet'

urlpatterns = [
    path('', meet.index, name='index'),
    path('<int:session_id>/', include('session.urls', namespace='session')),
    path('add-session/', meet.display_add_form, name="display_add_form"),
    path('add/', meet.add, name="add"),
    path('delete/', meet.delete, name="delete"),
]