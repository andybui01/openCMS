from django.urls import path, include
from .views import session

app_name='session'

urlpatterns = [
    path('', session.index, name='index'),
    path('delete/', session.delete, name="delete_session"),
    path('add/', session.athlete_add, name="athlete_add"),
    path('add-athlete/', session.display_athlete_add, name="display_athlete_add")
]