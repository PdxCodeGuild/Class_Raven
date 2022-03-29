from django.shortcuts import render
from .models import Pokemon, PokemonType
from django.db.models import Q


def listview(request):
    names = Pokemon.objects.all()
    #types = PokemonType.objects.all()
    search_post = request.GET.get('search')
    if search_post:
        names = Pokemon.objects.filter(Q(name__icontains=search_post))
    else:
        names = Pokemon.objects.all()
    return render(request,'home.html',{'names':names})

def randomview(request):
    name=Pokemon.objects.order_by("?").first()
    return render(request,'random.html', {'name':name})