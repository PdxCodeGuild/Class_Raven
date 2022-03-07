from django.db.models import *
from colorful.fields import RGBColorField as ColorField

# Create your models here.
class Species(Model):
    class Meta:
        verbose_name_plural = 'Species'
    dexid = IntegerField(primary_key=True)
    url = URLField()
    name = CharField(max_length=25)
    type1 = ForeignKey('Typing', on_delete=SET_NULL, null=True, related_name='type1')
    type2 = ForeignKey('Typing', on_delete=SET_NULL, null=True, related_name='type2')
    sprite = URLField()
    ability1 = ForeignKey('Ability', on_delete=SET_NULL, null=True, related_name='ability1')
    ability2 = ForeignKey('Ability', on_delete=SET_NULL, null=True, related_name='ability2')
    hidden_ability = ForeignKey('Ability', on_delete=SET_NULL, null=True, related_name='hidden_ability')
    height = DecimalField(default=0, decimal_places=2, max_digits=5)
    weight = DecimalField(default=0, decimal_places=2, max_digits=5)
    hp = IntegerField(default=0)
    attack = IntegerField(default=0)
    s_attack = IntegerField(default=0)
    defense = IntegerField(default=0)
    s_defense = IntegerField(default=0)
    speed = IntegerField(default=0)
    def __str__(self):
        return self.name
    def stat_total(self):
        return self.hp + self.attack + self.s_attack + self.defense + self.s_defense + self.speed
    def get_data(query=False):
        import requests as api
        url = 'https://pokeapi.co/api/v2/pokemon/'
        if query:
            url += str(query)
        response = api.get(url)
        data = response.json()
        return data
    def get_list(filter=False, filter_type=False):
        from django.core.paginator import Paginator
        pokemon_list = Species.objects.all().order_by('dexid')
        if filter:
            if filter_type == 'typing':
                typing = Typing.objects.get(name=filter)
                if len(typing.pokemon.all()) == 0:
                    pokemon_list = Species.objects.filter(Q(type1=typing.typeid)|Q(type2=typing.typeid)).order_by('dexid')
                    for pokemon in pokemon_list:
                        try:
                            typing.pokemon.add(pokemon)
                            typing.save()
                        except:
                            print('\n\n\n\n\n\n\n\n\nno\n\n\n\n\n\n\n\n\n')
                else:
                    pokemon_list = typing.pokemon.all()
            elif filter_type == 'ability':
                ability = Ability.objects.get(name=filter)
                if len(ability.pokemon.all()) == 0:
                    pokemon_list = Species.objects.filter(Q(ability1=ability.abilityid)|Q(ability2=ability.abilityid)).order_by('dexid')
                    hidden = Species.objects.filter(hidden_ability=ability.abilityid).order_by('dexid')
                    for pokemon in pokemon_list:
                        try:
                            ability.pokemon.add(pokemon)
                            ability.save()
                        except:
                            print('\n\n\n\n\n\n\n\n\nno\n\n\n\n\n\n\n\n\n')
                    for pokemon in hidden:
                        try:
                            ability.pokemon.add(pokemon)
                            ability.save()
                        except:
                            print('\n\n\n\n\n\n\n\n\nno\n\n\n\n\n\n\n\n\n')
                else:
                    pokemon_list = ability.pokemon.all()
                    hidden = Species.objects.filter(hidden_ability=ability.abilityid).order_by('dexid')

                return (Paginator(pokemon_list, 18), hidden)
            
        return Paginator(pokemon_list, 18)
    def check_data(self):
        stats = [
            self.height,
            self.weight,
            self.hp,
            self.attack,
            self.s_attack,
            self.defense,
            self.s_defense,
            self.speed
        ]
        for stat in stats:
            if stat == 0:
                stats = None
        if self.sprite == 'x.com':
            sprite = None
        else:
            sprite = self.sprite
        details = [
            self.type1,
            sprite,
            self.ability1,
            stats
        ]
        return details
class Typing(Model):
    typeid = IntegerField(primary_key=True)
    url = URLField()
    name = CharField(max_length=25)
    color = ColorField(default='#000000')
    pokemon = ManyToManyField('Species')
    def __str__(self):
        return self.name
    def get_data(query=False):
        import requests as api
        url = 'https://pokeapi.co/api/v2/type/'
        if query:
            url += str(query)
        response = api.get(url)
        data = response.json()
        return data
class Ability(Model):
    abilityid = IntegerField(primary_key=True)
    url = URLField()
    name = CharField(max_length=25)
    pokemon = ManyToManyField('Species')
    def __str__(self):
        return self.name
    def get_data(query=False):
        return