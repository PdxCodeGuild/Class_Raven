
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


app_name = 'users_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('<str:username>/', views.userprofile, name='userprofile'),
    path('logout', views.logout, name='logout'),
    
]