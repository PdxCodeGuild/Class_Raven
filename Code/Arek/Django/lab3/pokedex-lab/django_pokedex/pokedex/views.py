from django.shortcuts import render, redirect
from .models import Pokemon, User

# Create your views here.

def home(request):
    pokemon = Pokemon.objects.all()
    context = {
        'allpokemon': pokemon

    }

    return render(request, 'pokedex/all.html', context)

def choice_pokemon(request):
    form = request.POST
    user_choice = form['search']
    pokes = Pokemon.objects.filter(name=user_choice)
    choices = {
        'pokes': pokes
    }
    print(user_choice)

    return render(request, 'pokedex/search.html', choices)
