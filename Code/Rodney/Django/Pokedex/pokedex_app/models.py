from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import TextField, IntegerField, FloatField
from django.db.models.fields.related import ManyToManyField



class PokemonType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    types = ManyToManyField(PokemonType, related_name='pokemon')

    def __str__(self):
        return self.name