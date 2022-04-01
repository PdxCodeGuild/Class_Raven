from django.core.management.base import BaseCommand
from django.db import models
import requests

from pokedex_app.models import Pokemon, PokemonType


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = 'https://raw.githubusercontent.com/PdxCodeGuild/Class_Raven/master/4%20Django/labs/03%20Pokedex/pokemon.json'

        Pokemon.objects.all().delete()
        response= requests.get(f'https://raw.githubusercontent.com/PdxCodeGuild/Class_Raven/master/4%20Django/labs/03%20Pokedex/pokemon.json')
        data=response.json()
        data=data['pokemon']

        for poke in data:
            number=poke['number']
            name = poke['name']
            height = poke['height']
            weight = poke['weight']
            image_front = poke['image_front']
            image_back = poke['image_back']
            types=poke['types']

            pokemon, create=Pokemon.objects.get_or_create(
                number=number,
                name=name,
                height=height,
                weight=weight,
                image_front=image_front,
                image_back=image_back,
                types=types
            )
            
            # for type in types:
            #     pokemon=PokemonType.objects.add(type)
            #     #pokemon.types.add(type)

            # print(f"{pokemon} is in the database.")
            











        # response = requests.get(url)

        # pokedex_data = response.json() #dict 'pokemon':[data I want as a list of dictionaries]
        # pokedex_data = pokedex_data['pokemon']#list of dictionaries

        #print(pokedex_data)
        # create a database entry for each pokemon
        # for loop to pull data from each individual pokemon dictionary
        # for pokemon in pokedex_data:
        #     #print(pokemon)
        #     #print(" ")
        #     number = pokemon['number']
        #     name = pokemon['name']
        #     height = pokemon['height']
        #     weight = pokemon['weight']
        #     image_front = pokemon['image_front']
        #     image_back = pokemon['image_back']
        #     types = pokemon['types']
        #     pokemon = Pokemon.objects.create(
        #         number=number,
        #         name=name,
        #         height=height,
        #         weight=weight,
        #         image_front=image_front,
        #         image_back=image_back,
        #         )
                #apparetly you need to save before adding manytomany data..I still don't know how to get it right
            #pokemon.add(types)
            #print(pokemon)
