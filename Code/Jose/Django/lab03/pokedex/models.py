from django.db import models
# Create your models here.

class PokemonType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=300)
    image_back = models.CharField(max_length=300)
    types = models.ManyToManyField(PokemonType, related_name='pokemontype', blank=True)
    url = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.name}'