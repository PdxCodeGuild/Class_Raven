from django.shortcuts import render
from .models import Pokemon

# Create your views here.
def index(request):
    """Takes in number or name of pokemon from navbar. Pulls list of all pokemon and filters against input. Returns search results or all Pokemonz."""
    
    pokemon = Pokemon.objects.all().order_by('number') # All pokemon in DB
    pokemon_search = request.POST.get('pokemon_search') # User request

    if pokemon_search is None:
        return render(request, 'index.html', {'pokemon':pokemon})

    if pokemon.filter(name__icontains=pokemon_search):
        pokemon = pokemon.filter(name__icontains=pokemon_search)
        return render(request, 'index.html', {'pokemon':pokemon})

    try:
        pokemon = pokemon.filter(number=pokemon_search)
        return render(request, 'index.html', {'pokemon':pokemon})

    except ValueError:
        return render(request, 'index.html', {'pokemon':pokemon})

def select_element(request, element_id):
    pokemon = Pokemon.objects.all().order_by('number')
    pokemon = pokemon.filter(types__name__icontains=element_id) # searches for element of pokemon
    return render(request, 'index.html', {'pokemon':pokemon})
