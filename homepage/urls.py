from django.urls import path, include
from .views import homepage

app_name='homepage'

urlpatterns = [
    path('', homepage.index, name='index')
]