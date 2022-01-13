from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Pokemon

# Create your views here.
def index(request):

    pokemon = Pokemon.objects.all().order_by('number')


    return render(request, 'index.html', {'pokemon':pokemon})
