from django.urls import path
from .views import *
app_name = 'SITE'
urlpatterns = [
    path('', home, name='home'),
    path('load', load_all, name='load_all'),
    path('search', search, name='search'),
    path('link/<str:species>', link, name='link'),

    path('pokemon/all/page/<int:page_number>', lists.all, name='all'),
    path('pokemon/all/page/<int:page_number>/<str:species>', details.pokemon, name='details'),

    path('pokemon/typings/', lists.typings, name='typings'),
    path('pokemon/typings/<str:filter>/page/<int:page_number>', filtered.by_type, name='by_type'),
    path('pokemon/typings/<str:filter>/page/<int:page_number>/<str:species>', details.pokemon_by_type, name='details_by_type'),

    path('pokemon/abilities/page/<int:page_number>', lists.abilities, name='abilities'),
    path('pokemon/abilities/<str:filter>/page/<int:page_number>', filtered.by_ability, name='by_ability'),
    path('pokemon/abilities/<str:filter>/page/<int:page_number>/<str:species>', details.pokemon_by_ability, name='details_by_ability'),
]