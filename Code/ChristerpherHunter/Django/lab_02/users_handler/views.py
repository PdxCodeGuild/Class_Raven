from audioop import reverse
from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserForms, UserAuthorizeForm


# Create your views here.

def register(request):
    """form for creating a new user; redirect to /profile/ after registering"""

    form = UserAuthorizeForm()

    if request.method =="GET":
        return render(request, 'register.html', {"form": form})
    
    form = UserAuthorizeForm(data=request.POST)

    if form.is_valid():
        new_user = form.save(commit=False)

        new_user.set_password(form.cleaned_data['password'])

        new_user.save()

        return redirect(reverse('users_handler:regsiter'))
    
    context = {
        "form": UserAuthorizeForm(),
        "errors": form.errors,
    }

    return render(request, "users_handler/register.html", context)


def login(request):
    """form for logging a user in;redirect to /profile/ after logging in"""

    if request.user.is_authenticated:
        return HttpResponseRedirect('login.html')
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'forms': form})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                print('User not found')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'login.html', {'forms': form})
  

def profile(request):
    """form for logging a user in; redirect to /profile/ after logging in"""

    return render(request, "profile.html")