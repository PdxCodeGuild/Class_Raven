from django.db.models import *

# Create your models here.

class Pokemon(Model):
    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemon'
    dexid = IntegerField()
    # url = URLField(required=False)
    species = CharField(max_length=20)
    stats = JSONField()
    images = JSONField()
    type1 = CharField(max_length=10)
    type2 = CharField(max_length=10)
    ability1 = CharField(max_length=25)
    ability2 = CharField(max_length=25)
    hidden_ability = CharField(max_length=25)
    def __str__(self):
        return f'#{self.dexid} - {self.species.title()}'
    def typings_string(self):
        if self.type2 != 'False':
            return f'a {self.type1} and {self.type2} type pokemon.'
        else:
            return f'a {self.type1} type pokemon.'
    def abilities_string(self):
        string = f'abilit'
        if self.ability2 != 'False':
            string += f'ies: {self.ability1}, {self.ability2}'
        else:
            string += f'y: {self.ability1}'
        return string
    def hidden_ability_string(self):
        if self.hidden_ability != 'False':
            return f'hidden: {self.hidden_ability}'
    def height(self):
        stat = self.stats['height']
        return f'height: {stat}m'
    def weight(self):
        stat = self.stats['weight']
        return f'weight: {stat}kg'
    def sprite(self):
        sprite = self.images['standard']
        return sprite    
    def shiny_sprite(self):
        sprite = self.images['shiny']
        return sprite


class Typing(Model):
    typeid = IntegerField()
    symbol = ImageField()
    # url = URLField()
    name = CharField(max_length=10)
    immunities = CharField(max_length=10)
    weaknesses = CharField(max_length=10)
    strengths = CharField(max_length=10)
    def __str__(self):
        return f'{self.name}'

class Ability(Model):
    class Meta:
        verbose_name = 'Ability'
        verbose_name_plural = 'Abilities'
    abilityid = IntegerField()
    name = CharField(max_length=25)
    # url = URLField()
    description = TextField()
    def __str__(self):
        return f'{self.name}'