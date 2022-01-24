from django.db import models
from django.urls import reverse


class PokemonType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    image_front = models.ImageField(blank=True, upload_to='images_front/')
    image_back = models.ImageField(blank=True, upload_to='images_back/')
    types = models.ManyToManyField('PokemonType', blank=True)

    def __str__(self):
        return f"Entry: {self.number} | Name: {self.name} | Type: {self.types}"

    def get_absolute_url(self):
        return reverse('profile')