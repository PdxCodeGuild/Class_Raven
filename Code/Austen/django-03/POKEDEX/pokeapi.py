from urllib import response
import requests as api
import json

class urls:
    base = 'https://pokeapi.co/api/v2/'
    pokemon = base + 'pokemon/'
    typing = base + 'type/'
    ability = base + 'ability/'

class retrieve:
    def count():
        url = urls.pokemon
        response = api.get(url)
        data = response.json()
        return data['count']
    def pokemon(dexid):
        url = urls.pokemon + str(dexid)
        response = api.get(url)
        data = response.json()
        return data
    def typing(typeid):
        url = urls.typing + str(typeid)
        response = api.get(url)
        data = response.json()
        return data
    def ability(abilityid):
        url = urls.ability + str(abilityid)
        response = api.get(url)
        data = response.json()
        return data

class extract:
    def pokemon(data):
        # print(data.keys())
        # ['abilities', 'base_experience', 'forms', 'game_indices', 'height', 'held_items', 
        # 'id', 'is_default', 'location_area_encounters', 'moves', 'name', 'order', 'past_types', 
        # 'species', 'sprites', 'stats', 'types', 'weight']
        extracted = [
            data['id'],
            data['name'],
            {'height': data['height'], 'weight': data['weight']},
            extract.sprites(data['sprites']),
            extract.typings(data['types']),
            extract.abilities(data['abilities'])
        ]
        return extracted
    def sprites(data):
        # print(data.keys())
        extracted = [
            data['front_default'],
            data['front_shiny']
            ]
        return extracted    
    def typing(data):
        
        print(data.keys())
        print()
        relations = data['damage_relations']
        immunities = relations['no_damage_from']
        strengths = relations['half_damage_from']
        weaknesses = relations['double_damage_from']
        extracted = [
            data['name'],
            extract.typing_names(immunities),
            extract.typing_names(strengths),
            extract.typing_names(weaknesses),
        ]
        return extracted
    def typing_names(data):
        extracted = []
        for typing in data:
            extracted.append(typing['name'])
        return extracted
    def typings(data):
        # print(data)
        extracted = []
        for typing in data:
            typing = typing['type']
            typing = typing['name']
            extracted.append(typing)
        if len(extracted) == 1:
            extracted.append(False)
        return extracted
    def ability(data):
        extracted = [
            data['name'],
            ]
        for entry in data['effect_entries']:
            lang = entry['language']
            if lang['name'] == 'en':
                extracted.append(entry['effect'])
        return extracted
    def abilities(data):
        # print(data)
        extracted = []
        for ability in data:
            hidden = ability['is_hidden']
            ability = ability['ability']
            ability = ability['name']
            if hidden:
                if len(extracted) == 1:
                    extracted.append(False)
                    extracted.append(ability)
                else:
                    extracted.append(ability)
            else:
                extracted.append(ability)
        while len(extracted) < 3:
            extracted.append(False)

        return extracted

class create:
    def pokemon(data):
        from .models import Pokemon
        dexid=data[0]
        species=data[1]
        stats = data[2]
        sprites = data[3]
        typings = data[4]
        abilities = data[5]
        created = Pokemon.objects.create(
            dexid = dexid, 
            species = species, 
            stats = {'height': stats['height'] / 10, 'weight': stats['weight'] / 10}, 
            images = {'standard': sprites[0], 'shiny': sprites[1]},
            type1 = typings[0],
            type2 = typings[1],
            ability1 = abilities[0],
            ability2 = abilities[1],
            hidden_ability = abilities[2],
        )
        return created
    def typing(index, data):
        from .models import Typing
        created = Typing.objects.create(
            typeid = index,
            name = data[0],
            immunities = data[1],
            strengths = data[2],
            weaknesses = data[3]
        )
        return created
    def ability(index, data):
        from .models import Ability
        created = Ability.objects.create(
            abilityid = index,
            name = data[0],
            description = data[1]
        )
        return created