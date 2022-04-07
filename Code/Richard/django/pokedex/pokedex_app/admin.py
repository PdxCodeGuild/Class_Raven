from django.contrib import admin
from .models import Pokemon, PokemonType
class InlineModelAdmin(admin.ModelAdmin):
    #Pokemon.types(ModelAdmin.filter_horizontal)
    pass

# Register your models here.
admin.site.register([Pokemon])
admin.site.register([PokemonType])