from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import authenticate, login as django_login #import login as a different name.

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = request.POST
        login_username = form['Username']
        login_password = form['Password']
    return render(request, 'myapp/login.html')

def register_page(request):

    return render(request, 'myapp/register.html')


def register(request):
    
    form = request.POST
    register_username = form['Username']
    register_password = form['Password']
    new_user = User.objects.create_user(username=register_username, password=register_password)
    
    django_login(request)
    return redirect('myapp:profile')

@login_required
def profile(request):
    

    return render(request, 'myapp/profile.html')
