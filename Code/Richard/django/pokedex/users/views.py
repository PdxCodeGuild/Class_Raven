from django.shortcuts import render
from django.http import HttpResponse
from pokedex_app.models import Pokemon, PokemonType

# Create your views here.

def pokedex_view(request):
    my_pokemon=Pokemon.objects.all()
    context= {
        'my_pokemon':my_pokemon
    }
    return render(request, 'users/home.html', context)