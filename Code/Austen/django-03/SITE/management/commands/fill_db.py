from django.core.management.base import BaseCommand
from POKEDEX.models import *

class Command(BaseCommand):

    def handle(self, *args, **options):
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
        pokemon_list = Species.objects.all()
        for pokemon in pokemon_list:
            print(f'loading {pokemon.name}')
            details = pokemon.check_data()
            if None in details:
                pokemon.update_data(details)
        print('filled db')