from django.urls import path
from . import views

app_name='lifters'

urlpatterns = [
    path('', views.results, name='results'),
    path('admin/', views.admin, name='admin'),
    path('create/', views.create, name='create'),
    path('clear/', views.clear, name='clear'),
    path('<int:athlete_id>/remove/', views.remove, name='remove')
]
