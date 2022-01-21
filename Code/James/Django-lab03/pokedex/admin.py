from django.contrib import admin

from pokedex.models import Pokemon, PokemonType

# Register your models here.

admin.site.register([PokemonType, Pokemon])
