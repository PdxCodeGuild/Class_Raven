from django.core.management.base import BaseCommand
import requests
from pokedex_app.models import Pokemon, PokemonType
import json 

class Command(BaseCommand):

    def handle(self, *args, **options):
    
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()

        with open('static/pokemon.json') as pokemon_file:
            pokemons = json.loads(pokemon_file.read())
            for pokemon in pokemons['pokemon']:
                number = int(pokemon['number'])
                name = pokemon['name']
                height = float(pokemon['height'])
                weight = float(pokemon['weight'])
                image_front = pokemon['image_front']
                image_back = pokemon['image_back']
                types = pokemon['types']
                url = pokemon['url']

                pokemon = Pokemon.objects.create(
                    number = number,
                    name = name,
                    height = height,
                    weight = weight,
                    image_front = image_front,
                    image_back = image_back,
                    url = url
                )
                                    
                for type in types:
                    type, created = PokemonType.objects.get_or_create(name=type)

                    if type not in pokemon.types.all():
                        pokemon.types.add(type)

                


            