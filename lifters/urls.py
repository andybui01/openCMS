from django.urls import path
from lifters.views import *

urlpatterns = [
    path('', results),
    path('admin/', admin),
    path('create/', create)
]
