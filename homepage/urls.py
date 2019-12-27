from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import homepage

app_name='homepage'

urlpatterns = [
    path('', homepage.index, name='index'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('admin/', homepage.admin, name="admin"),
    path('admin/add/', homepage.add, name="add"),
    path('test/', homepage.test, name='test'),
    path('redirect-meet/', homepage.redirect_meet, name="redirect_meet")
]