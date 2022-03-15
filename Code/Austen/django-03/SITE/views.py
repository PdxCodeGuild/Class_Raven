from django.shortcuts import render
from POKEDEX.models import *
from .forms import *
from django.core.paginator import Paginator
# Create your views here.
def home(REQUEST):
    data = Species.get_data(query='?limit=898')
    for pokemon in data['results']:
        url = pokemon['url']
        dexid = url.replace('https://pokeapi.co/api/v2/pokemon/', '')
        dexid = dexid.replace('/', '')
        name = pokemon['name']
        Species.objects.get_or_create(dexid=dexid, url=url, name=name)
    data = Typing.get_data()
    for typing in data['results']:
        url = typing['url']
        typeid = url.replace('https://pokeapi.co/api/v2/type/', '')
        typeid = typeid.replace('/', '')
        name = typing['name']
        if name != 'shadow':
            Typing.objects.get_or_create(typeid=typeid, url=url, name=name)
    return render(REQUEST, 'home.html')
def load_all(REQUEST):
    pokemon_list = Species.objects.all()
    for pokemon in pokemon_list:
        print(f'loading {pokemon.name}')
        details = pokemon.check_data()
        if None in details:
            pokemon.update_data(details)
    return render(REQUEST, 'home.html')
def search(REQUEST):
    context = {
        'form': Search.by_species_name()
    }
    if REQUEST.POST:
        try:
            pokemon = Species.objects.get(name=REQUEST.POST['name'])
            pokemon_list = Species.get_list()
            context = {
                'page_number': (pokemon.dexid // 18) + 1,
                'list': pokemon_list.page((pokemon.dexid // 18) + 1),
                'list_type': 'pokemon',
                'pokemon': pokemon,
                }
        except:
            context.update({'error':'Pokemon not found'})
    return render(REQUEST, 'home.html', context)
def link(REQUEST, species):
    try:
        pokemon = Species.objects.get(name=species)
        pokemon_list = Species.get_list()
        context = {
            'page_number': (pokemon.dexid // 18) + 1,
            'list': pokemon_list.page((pokemon.dexid // 18) + 1),
            'list_type': 'pokemon',
            'pokemon': pokemon,
            }
    except:
        context.update({'error':'Pokemon not found'})
    return render(REQUEST, 'home.html', context)
class lists:
    def all(REQUEST, page_number):
        pokemon_list = Species.get_list()
        context = {
            'page_number': page_number,
            'list': pokemon_list.page(page_number),
            'list_type': 'pokemon'
        }
        return render(REQUEST, 'home.html', context)
    def typings(REQUEST):
        typing_list = Typing.objects.all().order_by('typeid')
        context = {
            'list_type': 'typings',
            'list': typing_list
        }
        return render(REQUEST, 'home.html', context)
    def abilities(REQUEST, page_number):
        abilities = Ability.objects.all().order_by('name')
        ability_list = Paginator(abilities, 12)
        context = {
            'list_type': 'abilities',
            'page_number': page_number,
            'list': ability_list.page(page_number)
        }
        return render(REQUEST, 'home.html', context)
class filtered:
    def by_type(REQUEST, filter, page_number):
        pokemon_list = Species.get_list(filter=filter, filter_type='typing')
        context = {
            'list_type': 'pokemon',
            'url': 'SITE:details_by_type',
            'url_page': 'SITE:by_type',
            'filter': filter,
            'page_number': page_number,
            'list': pokemon_list.page(page_number)
        }
        return render(REQUEST, 'home.html', context)
    def by_ability(REQUEST, filter, page_number):
        pokemon_lists = Species.get_list(filter=filter, filter_type='ability')
        pokemon_list = pokemon_lists[0]
        hidden = pokemon_lists[1]
        context = {
            'list_type': 'pokemon',
            'url': 'SITE:details_by_ability',
            'url_page': 'SITE:by_ability',
            'filter': filter,
            'page_number': page_number,
            'list': pokemon_list.page(page_number),
            'hidden_list': hidden
        }
        return render(REQUEST, 'home.html', context)
class details:
    def pokemon(REQUEST, page_number, species):
        pokemon = Species.objects.get(name=species)
        pokemon_list = Species.get_list()
        details = pokemon.check_data()
        if None in details:
            pokemon.update_data(pokemon, details)
        context = {
            'list_type': 'pokemon',
            'page_number': page_number,
            'list': pokemon_list.page(page_number),
            'pokemon': pokemon,

        }
        return render(REQUEST, 'home.html', context)
    def pokemon_by_type(REQUEST, filter, page_number, species):
        pokemon = Species.objects.get(name=species)
        pokemon_list = Species.get_list(filter=filter, filter_type='typing')
        details = pokemon.check_data()
        if None in details:
            data = Species.get_data(query=pokemon.dexid)
            if details[0] == None:
                typing = data['types']
                type1 = typing[0]
                type1 = type1['type']
                type1 = type1['name']
                type1 = Typing.objects.get(name=type1)
                pokemon.type1 = type1
                try:
                    type2 = typing[1]
                    type2 = type2['type']
                    type2 = type2['name']
                    type2 = Typing.objects.get(name=type2)
                    pokemon.type2 = type2
                except:
                    pass
            if details[1] == None:
                sprites = data['sprites']
                sprite = sprites['front_default']
                pokemon.sprite = sprite
            if details[2] == None:
                abilities = data['abilities']
                standard = []
                hidden = []
                for ability in abilities:
                    is_hidden = ability['is_hidden']
                    slot = ability['slot']
                    ability = ability['ability']
                    name = ability['name']
                    url = ability['url']
                    abilityid = url.replace('https://pokeapi.co/api/v2/ability/', '')
                    abilityid = abilityid.replace('/', '')
                    ability = Ability.objects.get_or_create(abilityid=abilityid, name=name, url=url)
                    ability = ability[0]
                    if is_hidden:
                        hidden.append(ability)
                    else:
                        standard.append(ability)
                pokemon.ability1 = standard[0]
                try:
                    pokemon.ability2 = standard[1]
                except:
                    pass
                try:
                    pokemon.hidden_ability = hidden[0]
                except:
                    pass
            if details[3] == None:
                pokemon.height = (data['height']/10)
                pokemon.weight = (data['weight']/10)
                stats = data['stats']
                for stat in stats:
                    value = stat['base_stat']
                    stat = stat['stat']
                    name = stat['name']
                    if name == 'hp':
                        pokemon.hp = value
                    elif name == 'attack':
                        pokemon.attack = value
                    elif name == 'special-attack':
                        pokemon.s_attack = value
                    elif name == 'defense':
                        pokemon.defense = value
                    elif name == 'special-defense':
                        pokemon.s_defense = value
                    elif name == 'speed':
                        pokemon.speed = value
            pokemon.save()
        context = {
            'list_type': 'pokemon',
            'url': 'SITE:details_by_type',
            'url_page': 'SITE:by_type',
            'filter': filter,
            'page_number': page_number,
            'list': pokemon_list.page(page_number),
            'pokemon': pokemon,

        }
        return render(REQUEST, 'home.html', context)
    def pokemon_by_ability(REQUEST, filter, page_number, species):
        pokemon = Species.objects.get(name=species)
        pokemon_lists = Species.get_list(filter=filter, filter_type='ability')
        pokemon_list = pokemon_lists[0]
        hidden_list = pokemon_lists[1]
        details = pokemon.check_data()
        if None in details:
            data = Species.get_data(query=pokemon.dexid)
            if details[0] == None:
                typing = data['types']
                type1 = typing[0]
                type1 = type1['type']
                type1 = type1['name']
                type1 = Typing.objects.get(name=type1)
                pokemon.type1 = type1
                try:
                    type2 = typing[1]
                    type2 = type2['type']
                    type2 = type2['name']
                    type2 = Typing.objects.get(name=type2)
                    pokemon.type2 = type2
                except:
                    pass
            if details[1] == None:
                sprites = data['sprites']
                sprite = sprites['front_default']
                pokemon.sprite = sprite
            if details[2] == None:
                abilities = data['abilities']
                standard = []
                hidden = []
                for ability in abilities:
                    is_hidden = ability['is_hidden']
                    slot = ability['slot']
                    ability = ability['ability']
                    name = ability['name']
                    url = ability['url']
                    abilityid = url.replace('https://pokeapi.co/api/v2/ability/', '')
                    abilityid = abilityid.replace('/', '')
                    ability = Ability.objects.get_or_create(abilityid=abilityid, name=name, url=url)
                    ability = ability[0]
                    if is_hidden:
                        hidden.append(ability)
                    else:
                        standard.append(ability)
                pokemon.ability1 = standard[0]
                try:
                    pokemon.ability2 = standard[1]
                except:
                    pass
                try:
                    pokemon.hidden_ability = hidden[0]
                except:
                    pass
            if details[3] == None:
                pokemon.height = (data['height']/10)
                pokemon.weight = (data['weight']/10)
                stats = data['stats']
                for stat in stats:
                    value = stat['base_stat']
                    stat = stat['stat']
                    name = stat['name']
                    if name == 'hp':
                        pokemon.hp = value
                    elif name == 'attack':
                        pokemon.attack = value
                    elif name == 'special-attack':
                        pokemon.s_attack = value
                    elif name == 'defense':
                        pokemon.defense = value
                    elif name == 'special-defense':
                        pokemon.s_defense = value
                    elif name == 'speed':
                        pokemon.speed = value
            pokemon.save()
        context = {
            'list_type': 'pokemon',
            'url': 'SITE:details_by_ability',
            'url_page': 'SITE:by_ability',
            'filter': filter,
            'page_number': page_number,
            'list': pokemon_list.page(page_number),
            'hidden_list': hidden_list,
            'pokemon': pokemon,

        }
        return render(REQUEST, 'home.html', context)