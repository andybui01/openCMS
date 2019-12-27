from django.urls import path, include
from .views import meet

app_name='meet'

urlpatterns = [
    path('', meet.index, name='index'),
    path('<int:session_id>/', include('session.urls', namespace='session')),
    path('delete/', meet.delete, name="delete"),
]