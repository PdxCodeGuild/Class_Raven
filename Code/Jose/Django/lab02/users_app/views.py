from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from users_app.models import User
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, "register.html")

    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        new_user = User.objects.create_user(username=username, password=password)

        django_login(request, new_user)
        return redirect(reverse("users_app:register"))

    else:

        return render(request, "register.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    elif request.method == "POST":
        form = request.POST
        username = form["username"]
        password = form["password"]
        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {
                "errors": ["Invalid Username or Password"],
            }

            return render(request, "login.html", context)

        else:
            django_login(request, user)
            return HttpResponseRedirect(reverse("users_app:profile", kwargs={"username": user.username}))


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, "profile.html", {"user": user})



def logout(request):
    django_logout(request)
    return redirect(reverse("users_app:login"))