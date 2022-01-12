from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, PokemonType, Pokemon
# Register your models here.

admin.site.register(User, UserAdmin) # need this if you are going to have users in your ap
admin.site.register(Pokemon)
admin.site.register(PokemonType)
