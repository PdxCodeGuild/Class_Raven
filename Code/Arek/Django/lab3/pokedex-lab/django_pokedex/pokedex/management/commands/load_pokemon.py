from django.core.management.base import BaseCommand
import requests
import json
from pokedex.models import Pokemon, PokemonType

class Command(BaseCommand):


    def handle(self, *args, **options):
        PokemonType.objects.all().delete()
        Pokemon.objects.all().delete() # this will clear the table so that each time this command is ran,
        # we dont add 152 more entries to the DB

        with open('pokedex/management/commands/pokemon.json', 'r') as f:
            contents = f.read()
            contents = json.loads(contents) # this turns the json into a python dictionary
        poke_num = 152
        for i in range(1, poke_num - 1): # this loops through all the pokemon in the converted dictionary
            print(contents['pokemon'][i]['name'])

            """
                number = models.IntegerField()
                name = models.CharField(max_length=20)
                height = models.FloatField(default=0.0)
                weight = models.FloatField(default=0.0)
                image_front = models.CharField(max_length=100)
                image_back = models.CharField(max_length=100)
                types = models.ManyToManyField(PokemonType)
            
            """
            
            pknumber = contents['pokemon'][i]['number']
            pkname = contents['pokemon'][i]['name']
            pkheight = contents['pokemon'][i]['height']
            pkweight = contents['pokemon'][i]['weight']
            pk_image_front = contents['pokemon'][i]['image_front']
            pk_image_back = contents['pokemon'][i]['image_back']
            pktypes = contents['pokemon'][i]['types']
            pkdescription = contents['pokemon'][i]['url']

            
            new_pokemon = Pokemon.objects.create(
                number=pknumber, 
                name=pkname, height=pkheight, 
                weight=pkweight, 
                image_front=pk_image_front, 
                image_back=pk_image_back, 
                description=pkdescription
                )

            for item in pktypes:
                new_pokemon_types, created = PokemonType.objects.get_or_create(name=item)
                new_pokemon.types.add(new_pokemon_types)

            #Right now the each pokemons types are either a single one or something like this
            # ['flying', 'fire'] But it the types should all be a single entry, and if a pokemon has
            # more than one type then it should more than one thing highlighted.
            #Need to loop through the list and add each type, if its already been created, thats why we use get_or_create
            """new_pokemon_types, created = PokemonType.objects.get_or_create(name=pktype)
            new_pokemon.types.add(new_pokemon_types)"""
            

        
        
        
        