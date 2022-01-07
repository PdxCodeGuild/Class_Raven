from django.shortcuts import render
from django.http import HttpResponse as HTTP

# Create your views here.


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
