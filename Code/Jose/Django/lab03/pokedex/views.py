from .models import Pokemon, PokemonType
from django.shortcuts import render
# Create your views here.

def home(request):
    pokemon = Pokemon.objects.all().order_by('number')
    pokemon_type = PokemonType.objects.all()
    context = {
        'pokemon': pokemon,
        'pokemon_type': pokemon_type,
    }
    return render(request, 'index.html', context)