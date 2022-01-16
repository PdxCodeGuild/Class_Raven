from base64 import urlsafe_b64decode
import py_compile
from turtle import title
from django.contrib import auth
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import PokemonType, Pokemon 
from django.db.models import Q
from django.core.paginator import Paginator


def home(request, page_num=1, per_page=10):

    form = {
        'search_name': request.POST.get('search_name') or '',
        # 'types': request.POST.getlist('types') or [type.name for type in PokemonType.objects.all()],
    }

    search_name = form.get('search_name')
    # search_types = form.get('types')

    pokemons = Pokemon.objects.all()

    # if search_types:
    #     pokemons = Pokemon.objects.filter(types__name__in=search_types)

    if search_name: 
        pokemons = pokemons.filter(name__icontains=search_name)

    for pokemon in pokemons:
        pokemon.weight = (pokemon.weight/10) * 2.2
        pokemon.weight = int(pokemon.weight)
    
    for pokemon in pokemons:
        pokemon.height = (pokemon.height/10) * 39.37
        pokemon.height = int(pokemon.height)
        if pokemon.height > 12:
            pokemon_feet = pokemon.height//12
            pokemon_inches = pokemon.height%12
            pokemon.height = (f'{pokemon_feet} ft. {pokemon_inches} in.')
        else:
            pokemon.height = (f'{pokemon.height} in.')


    for pokemon in pokemons:
        pokemon.type = pokemon.types.all()

    page_num = request.GET.get('page_num') or page_num
    per_page = request.GET.get('per_page') or per_page
    
    pokemons_page = Paginator(pokemons, per_page).get_page(page_num)

    context = {
        'pokemons_page': pokemons_page,  
    }
    
    return render(request, 'pokedex_home/home.html', context )


def heightup(request, page_num=1, per_page=10):
    
    page_num = request.GET.get('page_num') or page_num
    per_page = request.GET.get('per_page') or per_page

    pokemons = Pokemon.objects.all().order_by('-height')

    for pokemon in pokemons:
        pokemon.weight = (pokemon.weight/10) * 2.2
        pokemon.weight = int(pokemon.weight)
    
    for pokemon in pokemons:
        pokemon.height = (pokemon.height/10) * 39.37
        pokemon.height = int(pokemon.height)
        if pokemon.height > 12:
            pokemon_feet = pokemon.height//12
            pokemon_inches = pokemon.height%12
            pokemon.height = (f'{pokemon_feet} ft. {pokemon_inches} in.')
        else:
            pokemon.height = (f'{pokemon.height} in.')

    for pokemon in pokemons:
        pokemon.type = pokemon.types.all()

    pokemons_page = Paginator(pokemons, per_page).get_page(page_num)

    print(per_page)

    context = {
        'pokemons_page': pokemons_page,  
    }
    return render(request, 'pokedex_home/home.html', context )

def heightdown(request, page_num=1, per_page=10):
    
    page_num = request.GET.get('page_num') or page_num
    per_page = request.GET.get('per_page') or per_page

    pokemons = Pokemon.objects.all().order_by('height')

    for pokemon in pokemons:
        pokemon.weight = (pokemon.weight/10) * 2.2
        pokemon.weight = int(pokemon.weight)
    
    for pokemon in pokemons:
        pokemon.height = (pokemon.height/10) * 39.37
        pokemon.height = int(pokemon.height)
        if pokemon.height > 12:
            pokemon_feet = pokemon.height//12
            pokemon_inches = pokemon.height%12
            pokemon.height = (f'{pokemon_feet} ft. {pokemon_inches} in.')
        else:
            pokemon.height = (f'{pokemon.height} in.')

    for pokemon in pokemons:
        pokemon.type = pokemon.types.all()

    pokemons_page = Paginator(pokemons, per_page).get_page(page_num)

    context = {
        'pokemons_page': pokemons_page,  
    }
    return render(request, 'pokedex_home/home.html', context )

def weightup(request, page_num=1, per_page=10):
    
    page_num = request.GET.get('page_num') or page_num
    per_page = request.GET.get('per_page') or per_page

    pokemons = Pokemon.objects.all().order_by('-weight')

    for pokemon in pokemons:
        pokemon.weight = (pokemon.weight/10) * 2.2
        pokemon.weight = int(pokemon.weight)
    
    for pokemon in pokemons:
        pokemon.height = (pokemon.height/10) * 39.37
        pokemon.height = int(pokemon.height)
        if pokemon.height > 12:
            pokemon_feet = pokemon.height//12
            pokemon_inches = pokemon.height%12
            pokemon.height = (f'{pokemon_feet} ft. {pokemon_inches} in.')
        else:
            pokemon.height = (f'{pokemon.height} in.')

    for pokemon in pokemons:
        pokemon.type = pokemon.types.all()

    pokemons_page = Paginator(pokemons, per_page).get_page(page_num)

    context = {
        'pokemons_page': pokemons_page,  
    }
    return render(request, 'pokedex_home/home.html', context )

def weightdown(request, page_num=1, per_page=10):
    
    page_num = request.GET.get('page_num') or page_num
    per_page = request.GET.get('per_page') or per_page

    pokemons = Pokemon.objects.all().order_by('weight')

    for pokemon in pokemons:
        pokemon.weight = (pokemon.weight/10) * 2.2
        pokemon.weight = int(pokemon.weight)
    
    for pokemon in pokemons:
        pokemon.height = (pokemon.height/10) * 39.37
        pokemon.height = int(pokemon.height)
        if pokemon.height > 12:
            pokemon_feet = pokemon.height//12
            pokemon_inches = pokemon.height%12
            pokemon.height = (f'{pokemon_feet} ft. {pokemon_inches} in.')
        else:
            pokemon.height = (f'{pokemon.height} in.')

    for pokemon in pokemons:
        pokemon.type = pokemon.types.all()

    pokemons_page = Paginator(pokemons, per_page).get_page(page_num)

    context = {
        'pokemons_page': pokemons_page,  
    }
    return render(request, 'pokedex_home/home.html', context )



