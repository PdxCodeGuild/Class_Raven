from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('user/login', views.login, name='login'),
    path('user/register', views.register, name='register'),
]
