from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import *
from .pokeapi import *
from .utils import *
# Create your views here.

class pokemon:
    def by_filter(REQUEST, filter, page_number):
        pokemon_list = get_pokemon_list(filter)
        hidden_list = get_pokemon_list(filter, hidden=True)
        print(pokemon_list)
        page_limit = 12
        pokemon_list = Paginator(pokemon_list, page_limit)
        context = {
            'list': pokemon_list.page(page_number),
            'hidden': hidden_list,
            'list_type': 'pokemon',
            'filter': filter,
            'prev_page': page_number - 1,
            'page_number': page_number,
            'next_page': page_number + 1,            
            'last_page': pokemon_list.num_pages - 1,
            'pages': pokemon_list.num_pages
            }
        return render(REQUEST, 'home.html', context)
    def details(REQUEST, filter, page_number, species):
        pokemon_list = get_pokemon_list(filter)
        hidden_list = get_pokemon_list(filter, hidden=True)
        pokemon_list = Paginator(pokemon_list, 12)
        context = {
            'list': pokemon_list.page(page_number),
            'hidden': hidden_list,
            'list_type': 'pokemon',
            'filter': filter,
            'prev_page': page_number - 1,
            'page_number': page_number,
            'next_page': page_number + 1,
            'last_page': pokemon_list.num_pages - 1,
            'pages': pokemon_list.num_pages,
            'pokemon': Pokemon.objects.get(species=species)
        }
        return render(REQUEST, 'home.html', context)

class lists:
    def typings(REQUEST):
        typings = Typing.objects.all()
        count = 18
        if len(typings) < count:
            index = 1
            db_types = []
            for typing in typings:
                db_types.append(typing.typeid)
            while index <= count:
                if index not in db_types:
                    print(f'requesting type {index}/{count}')
                    data = retrieve.typing(index)
                    extracted = extract.typing(data)
                    created = create.typing(index, extracted)
                index += 1
            typings = Typing.objects.all()
        context = {
            'list': typings,
            'list_type': 'typings', 
            'page_number': 1
        }
        return render(REQUEST, 'home.html', context)
    def abilities(REQUEST):
        abilities = Ability.objects.all()
        count = 327
        count = 50
        if len(abilities) < count:
            index = 1
            db_abilities = []
            for ability in abilities:
                db_abilities.append(ability.abilityid)
            while index <= count:
                if index not in db_abilities:
                    print(f'requesting ability {index}/{count}')
                    data = retrieve.ability(index)
                    extracted = extract.ability(data)
                    created = create.ability(index, extracted)
                index += 1
            abilities = Ability.objects.all().order_by('name')
        context = {
            'list': abilities,
            'list_type': 'abilities', 
            'page_number': 1
        }
        return render(REQUEST, 'home.html', context)