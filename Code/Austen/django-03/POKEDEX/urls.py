from django.urls import path
from .views import *

app_name = "DEX"
urlpatterns = [
    path('pokemon/<str:filter>/page/<int:page_number>', pokemon.by_filter, name='pokemon'),
    path('pokemon/<str:filter>/page/<int:page_number>/<str:species>', pokemon.details, name='details'),
    path('types/all', lists.typings, name='typings'),
    path('abilities/all', lists.abilities, name='abilities'),
]