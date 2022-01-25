'''Django Lab03 Pokedex
By Philip Bartoo
January 15, 2022

Pokedex
Let's build a searchable pokedex! First we'll load the data from a json file into our own database. Then we'll list those pokemon in the page and add search.
The Pokédex (Japanese: ポケモン図鑑 illustrated Pokémon encyclopedia) is a digital encyclopedia for Trainers in the Pokémon world. It gives information about all Pokémon in the world that are contained in its database.
Pokédex entries typically describe a Pokémon in only two or three sentences. They may give background information on the habitat or activities of a Pokémon in the wild or other information on the Pokémon's history or anatomy.
Pokédex entries also include height, weight, cry, footprint, location, other forms, and a picture of the Pokémon.
Pokedex Wiki, Pokemon.com
Part 1
Create an app pokedex and add two models to store our pokemon, Pokemon and PokemonType.
PokemonType should have the following fields:
name (CharField)
Pokemon should have the following fields:
number (IntegerField)
name (CharField)
height (FloatField)
weight (FloatField)
image_front (CharField)
image_back (CharField)
types (ManyToManyField with PokemonType)
Part 2
Write a custom management command load_pokemon.py to load the data from pokemon.json into your database. You can do this by saving the file next to your .py file and using opening the file. To handle the types, check out many to many fields. In the first line of your management command, you may want to delete all the records in the table so each time you run it you start with a clean slate. To verify that the data was loaded, open your admin panel and check that the pokemon are there.
Part 3
Write a view, route and template to show a list of pokemon on the front page. You can either show all the information as a table, or show only their name and icon and link to a detail page with all their information. Use <img src="..."> to display their front and back image.
Part 4 (optional)
Check out the script that creates the json file, you can use it to load even more pokemon into your database!

Notes: This was my first Custom Management Command.
What really helped was looking at the raw JSON and writing down the structure to understand the nesting.
It's like peeling an onion back one layer at a time, where the key that picked the lock was accessing the 
first dictionary in the 'data=pokemon['pokemon']' code. The trickiest part is dealing with the types.
First, the types are a list nested within the dictionary for each item.  
'''

from django.core.management.base import BaseCommand, CommandError
from pokedex_app.models import Pokemon,PokemonType
#import requests
import json
#import pyperclip

class Command(BaseCommand):
    help = 'Imports Pokedex JSON'

    def handle(self, *args, **kwargs):

        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()
        
        file = open("pokemon.json")
        pokemon = json.load(file)
        data=pokemon['pokemon']
        
        for row in data:
            number=int(row['number'])
            name=row['name']
            height=int(row['height'])
            weight=int(row['weight'])
            image_front=row['image_front']
            image_back=row['image_back']
            type=row['types']
       
            #print(types)

            

            pokemon = Pokemon.objects.create(
                number=number,
                name=str.title(name),
                height=height,
                weight=weight,
                image_front=image_front,
                image_back=image_back
            )
            for type in type:
                type, created = PokemonType.objects.get_or_create(name=type)
                pokemon.types.add(type)
            #print('success??')
        
        
        #for row in pokemon:
            #pokemon = pokemon['pokemon']
            #name = row["Name"]
            #pokemon.name = row['Name']
            #pokemon.height = int(row['height'])
            #pokemon.weight = int(row['weight'])
            #pokemon.image_front = row['image_front']
            #pokemon.image_back = row['image_back']
            #pokemon.type = [type['type']['name'] for type in pokemon['types']]

        #file.close()

        #print(pokemon.type)
'''
        print('Creating Pokemon Type Data')
        for 

        url = 'https://pokeapi.co/api/v2/pokemon/3'
        response = requests.get(url)
        item = response.json()
        number = int(item['id'])
        name = item['name']
        types = [type['type']['name'] for type in item['types']]
        print(name, types)

        pokemontype, created = PokemonType.objects.get_or_create(id=number)
        print(pokemontype)

        data = {'pokemon':[]}
        num_pokemon = 1

        for i in range(1, num_pokemon):
# get the data from the pokemon api
            response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(i))
            pokeapi_data = json.loads(response.text)
            
# extract the relevant portions of data
            number = pokeapi_data['id']
            name = pokeapi_data['name']
            height = pokeapi_data['height']
            weight = pokeapi_data['weight']
            image_front = pokeapi_data['sprites']['front_default']
            image_back = pokeapi_data['sprites']['back_default']
            url = 'https://pokemon.fandom.com/wiki/' + name
            types = [type['type']['name'] for type in pokeapi_data['types']]

            pokemontype, created = PokemonType.objects.get_or_create(name=types)
            print(pokemontype)

    # put the relevant data into a dictionary
            pokemon = {
                'number': number,
                'name': name,
                'height': height,
                'weight': weight,
                'image_front': image_front,
                'image_back': image_back,
                'types': types,
                'url': url
            }

    # add the pokemon to our list
            data['pokemon'].append(pokemon)

    # give the user some feedback
            print(str(round(i/num_pokemon*100,2))+'%')

# copy the resulting json to the clipboard
        pyperclip.copy(json.dumps(data, indent=4))
'''