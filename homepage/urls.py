from django.urls import path, include
from .views import homepage

app_name='homepage'

urlpatterns = [
    path('', homepage.index, name='index'),
    path('test', homepage.test, name='test'),
    path('redirect-meet', homepage.redirect_meet, name="redirect-meet")
]