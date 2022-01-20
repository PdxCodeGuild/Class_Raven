from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


app_name = 'pokedex_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('heightup/', views.heightup, name='heightup'),
    path('heightdown/', views.heightdown, name='heightdown'),
    path('weightup/', views.weightup, name='weightup'),
    path('weightdown/', views.weightdown, name='weightdown'),
    
]

