from django.urls import path, include

from . import views

app_name = 'pokedex'

urlpatterns = [
    path('', views.home, name='home')

]

