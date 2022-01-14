from django.http.response import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Pokemon

# Create your views here.
def index(request):
    """Takes in number or name of pokemon from navbar. Pulls list of all pokemon and filters against input. Returns search results or all Pokemonz."""
    
    pokemon_universe = Pokemon.objects.all().order_by('number')
    pokemon_search = request.POST.get('pokemon_search')
    pokemon = ""

    if pokemon_search is None:
        pokemon = pokemon_universe
        return render(request, 'index.html', {'pokemon':pokemon})

    if pokemon_universe.filter(name__icontains=pokemon_search):
        pokemon = pokemon_universe.filter(name__icontains=pokemon_search)
        return render(request, 'index.html', {'pokemon':pokemon})

    else:
        pokemon = pokemon_universe

    try:
        pokemon = pokemon_universe.filter(number=pokemon_search)
        return render(request, 'index.html', {'pokemon':pokemon})

    except ValueError:
        return render(request, 'index.html', {'pokemon':pokemon})

    
