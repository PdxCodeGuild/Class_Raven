from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'myapp/userform.html')

def register(request):
    pass

def profile(request):
    pass
