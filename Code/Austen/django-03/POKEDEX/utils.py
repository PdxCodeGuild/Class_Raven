from .models import Pokemon
from django.db.models import Q
from .pokeapi import *

def get_pokemon_list(filter, hidden=False):
        if filter == 'all':
            pokemon_list = Pokemon.objects.all()
            count = 898
        elif hidden:
            pokemon_list = Pokemon.objects.filter(hidden_ability=filter)
            return pokemon_list
        else:
            try:
                pokemon_list = Pokemon.objects.filter(Q(type1=filter)|Q(type2=filter))
                if len(pokemon_list) == 0:
                    try:
                        pokemon_list = Pokemon.objects.filter(Q(ability1=filter)|Q(ability2=filter))
                    except:
                        pass
            except: 
                pass
            count = len(pokemon_list)
        if len(pokemon_list) < count:
            db_dexids = []
            for pokemon in pokemon_list:
                db_dexids.append(pokemon.dexid)
            index = 1
            while index <= count:
                if index not in db_dexids:
                    print(f'requesting type {index}/{count}')
                    data = retrieve.pokemon(index)
                    extracted = extract.pokemon(data)
                    print(extracted)
                    created = create.pokemon(extracted)
                    print(created)
                index += 1
        return pokemon_list