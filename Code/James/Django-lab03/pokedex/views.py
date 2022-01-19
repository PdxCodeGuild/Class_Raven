from django.shortcuts import (
    render, 
    get_object_or_404, 
    redirect
)


from .models import Pokemon, PokemonType

# Create your views here.
def home(request):
    pokemon = Pokemon.objects.all().order_by('number')
    pokemon_type = PokemonType.objects.all()
    context = {
        'pokemon': pokemon,
        'pokemon_type': pokemon_type,
    }
    return render(request, 'pokedex/index.html', context)