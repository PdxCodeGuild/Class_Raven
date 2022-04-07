from django.urls import path
from . import views

app_name= 'users'
urlpatterns=[
    path('', views.pokedex_view, name='pokedex_view')
]
