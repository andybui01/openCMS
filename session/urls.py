from django.urls import path, include
from .views import session

app_name='session'

urlpatterns = [
    path('', session.index, name='index'),
    path('manage/', session.manage, name='manage'),
    path('delete/', session.session_delete, name="session_delete"),
    path('add/', session.athlete_add, name="athlete_add"),
    path('add-athlete/', session.display_athlete_add, name="display_athlete_add"),
    path('delete/<int:athlete_id>/', session.athlete_delete, name="athlete_delete"),
    path('update-attempt/<int:athlete_id>', session.athlete_update, name="athlete_update")
]