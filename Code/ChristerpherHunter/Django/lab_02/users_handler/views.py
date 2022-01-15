from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect, redirect, reverse
from .forms import UserCreationsForm, UserForms, UserAuthorizeForm
from colorama import Fore as F

R = F.RESET


# Create your views here.

def register(request):
    """form for creating a new user; redirect to /profile/ after registering"""

    if request.method == "GET":
        form = UserCreationsForm()
        return render(request, 'register.html', {"form": form})

    form = UserCreationsForm(data=request.POST)

    if form.is_valid():
        new_user = form.save(commit=False)

        new_user.set_password(form.cleaned_data['password'])

        new_user.save()

        context = {
            "form": UserCreationsForm()
        }
        return render(request, 'register.html', context)

    context = {
        "form": UserCreationsForm(),
        "errors": form.errors,
    }
    print(f"{F.RED}{form.errors.as_json()}{R}")

    return render(request, "register.html", context)


def login(request):
    """form for logging a user in;redirect to /profile/ after logging in"""

    if request.method == "GET":
        form = UserAuthorizeForm()

        return render(request, 'login.html', {"form": form})

    form = UserAuthorizeForm(initial=request.POST)

    username = form.initial.get('username')[0]
    password = form.initial.get('password')[0]
    print(f"{F.BLUE}{username}{password}{R}")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        print(f"{F.GREEN}{user}{R}")
        django_login(request, user)
        return redirect(reverse('blog:index'))
    else:
        print(f'{F.RED}User not found{R}')
        print(f"{F.RED}Returning errors{R} {F.YELLOW}{form.errors}{R}")
        return render(request, 'login.html', {'errors': form.errors})


def profile(request):
    """form for logging a user in; redirect to /profile/ after logging in"""

    return render(request, "profile.html")
