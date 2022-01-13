from django.shortcuts import render, redirect
from .models import Pokemon

# Create your views here.

def home(request):
    pokemon = Pokemon.objects.all()
    context = {
        'allpokemon': pokemon

    }

    return render(request, 'pokedex/base.html', context)
