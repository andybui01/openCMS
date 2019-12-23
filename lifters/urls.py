from django.urls import path
from lifters.views import *

app_name='lifters'

urlpatterns = [
    path('', results, name='results'),
    path('admin/', admin, name='admin'),
    path('create/', create, name='create')
]
