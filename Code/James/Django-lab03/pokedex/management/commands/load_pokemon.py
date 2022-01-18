from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, PokemonType
import json

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('./pokedex/management/commands/pokemon.json', 'r') as f:
            contents = json.load(f)
            pokemon_dict = contents['pokemon']
            print(pokemon_dict)
            
            # f.read()
            
            for pokemon in pokemon_dict:
                number = pokemon['number']
                name = pokemon['name']
                height = pokemon['height']
                weight = pokemon['weight']
                image_front = pokemon['image_front']
                image_back = pokemon['image_back']
                types = pokemon['types']

                types, created = PokemonType.objects.get_or_create(name=types)
               
                pokemon = Pokemon.objects.create(
                    number=number,
                    name=name,
                    height=height,
                    weight=weight,
                    image_front=image_front,
                    image_back=image_back,
                    # types=all_types
                )

                
                Pokemon.types.add(types)

            