from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('<str:username>/', views.profile, name='profile'),
    

]