from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.

def register(request):
    """form for creating a new user; redirect to /profile/ after registering"""

    form = UserCreationForm()

    return render(request, 'register.html', {"form": form})


def login(request):
    """form for logging a user in;redirect to /profile/ after logging in"""

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
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