from django.core.management.base import BaseCommand
import requests

from pokedex_app.models import Pokemon, PokemonType


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = 'https://raw.githubusercontent.com/PdxCodeGuild/Class_Raven/master/4%20Django/labs/03%20Pokedex/pokemon.json'

        #Pokemon.objects.all().delete()

        for number in range(1, 151):
            response= requests.get(f'https://pokeapi.co/api/v2/pokemon/{number}')
            data=response.json()
            id=data['id']
            number=data['number']
            name = data['name']
            height = data['height']
            weight = data['weight']
            image_front = data['image_front']
            image_back = data['image_back']

        # response = requests.get(url)

        # pokedex_data = response.json() #dict 'pokemon':[data I want as a list of dictionaries]
        # pokedex_data = pokedex_data['pokemon']#list of dictionaries

        #print(pokedex_data)
        # create a database entry for each pokemon
        # for loop to pull data from each individual pokemon dictionary
        for pokemon in pokedex_data:
            #print(pokemon)
            #print(" ")
            number = pokemon['number']
            name = pokemon['name']
            height = pokemon['height']
            weight = pokemon['weight']
            image_front = pokemon['image_front']
            image_back = pokemon['image_back']
            types = pokemon['types']
            pokemon = Pokemon.objects.create(
                number=number,
                name=name,
                height=height,
                weight=weight,
                image_front=image_front,
                image_back=image_back,
                )
                #apparetly you need to save before adding manytomany data..I still don't know how to get it right
            #pokemon.add(types)
            #print(pokemon)
