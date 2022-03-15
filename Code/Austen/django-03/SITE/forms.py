from django.forms import *
from POKEDEX.models import *
class Search:
    class by_species_name(ModelForm):
        class Meta:
            model = Species
            fields = ['name']