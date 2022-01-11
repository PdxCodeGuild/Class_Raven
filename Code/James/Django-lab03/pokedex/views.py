from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Pokemon, PokemonType

# Create your views here.
def home(request):
    return render(request, 'pokedex/index.html')