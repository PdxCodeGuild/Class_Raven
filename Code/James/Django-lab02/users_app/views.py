from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth import (
    get_user_model,
    authenticate,
    login as django_login,
    logout as django_logout
)

from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserAuthForm

# Create your views here.
def register(request):
    form = UserAuthForm()
    
    if request.method == 'GET':
        
        context = {
            'form':form
        }

        return render(request, 'users/register.html', context)


def login(request):
    if request.method == 'GET':
        form = UserAuthForm()

        return render(request, 'users/login.html', {'form': form})


def profile(request, username):
    pass