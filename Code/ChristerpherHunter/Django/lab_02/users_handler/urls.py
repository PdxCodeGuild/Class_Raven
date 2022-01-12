from django.urls import path
from . import views

app_name = 'users_handler'
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
]