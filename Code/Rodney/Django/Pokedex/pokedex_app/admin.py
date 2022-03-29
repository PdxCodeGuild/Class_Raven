from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import PokemonType, Pokemon

admin.site.register(PokemonType)
admin.site.register(Pokemon)