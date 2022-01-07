from django.shortcuts import render
from django.http import HttpResponse as HTTP

# Create your views here.


def login(request):
    return HTTP('login view connected')


def register(request):
    return HTTP('register view connected')
