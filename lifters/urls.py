from django.urls import path
from .views import meet, session, athlete

app_name='lifters'

urlpatterns = [
    path('<int:meet_id>', meet.index, name='index'),
    path('<int:meet_id>/<int:session_id>/admin/', session.admin, name='admin'),
    path('<int:meet_id>/<int:session_id>/results/', session.results, name='results'),
    path('<int:meet_id>/<int:session_id>/create/', athlete.create, name='create'),
    path('<int:meet_id>/<int:session_id>/clear/', session.clear, name='clear'),
    path('<int:meet_id>/<int:session_id>/<int:athlete_id>/remove/', athlete.remove, name='remove'),
    path('<int:meet_id>/<int:session_id>/<int:athlete_id>/details/', athlete.details, name='details')
]
