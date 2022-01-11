from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class PokemonType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=100)
    image_back = models.CharField(max_length=100)
    types = models.ManyToManyField(PokemonType, related_name='type', blank=True)
    def __str__(self):
        return f'{self.name}'