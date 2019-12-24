from django.urls import path, include
from .views import session

app_name='session'

urlpatterns = [
    path('', session.index, name='index')
]