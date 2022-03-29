from django.core.management.base import BaseCommand
import requests
from pokedex.models import Pokemon, PokemonType
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()
        pokedex = open('/home/pop/Documents/pdx_code/Class_Raven/Code/Lee/Django/lab03/pokedex/management/commands/pokemon.json')
        pokedex = json.load(pokedex)
        for pokemon in pokedex['pokemon']:
            print(f"loading {pokemon['number']}. {pokemon['name']}")
            number = int(pokemon["number"])
            name = pokemon['name']
            height = int(pokemon['height'])
            weight = int(pokemon['weight'])
            image_front = pokemon['image_front']
            image_back = pokemon['image_back']
            types = pokemon['types']

            new_pokemon = Pokemon.objects.create(
                number=number,
                name=name,
                height=height,
                weight=weight,
                image_front=image_front,
                image_back=image_back,
            )

            for type in types:
                pokemon_type, created = PokemonType.objects.get_or_create(name=type.capitalize())
                new_pokemon.types.add(pokemon_type)