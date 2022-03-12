from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout,
)
from users.models import CustomUser


def register(request):
    if request.method == "GET":
        return render(request, "users/register.html")

    elif request.method == "POST":
        form = request.POST

        username = form["username"]
        password = form["password"]

        new_user = CustomUser.objects.create_user(
            username=username,
            password=password,
        )

        django_login(request, new_user)
        return HttpResponseRedirect(reverse("assistant:index"))


def login(request):
    if request.method == "GET":
        return render(request, "users/login.html")

    elif request.method == "POST":
        form = request.POST

        username = form["username"]
        password = form["password"]

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(
                request, "users/login.html", {"error": "Invalid Username or Password!"}
            )

        django_login(request, user)
        return HttpResponseRedirect(reverse("assistant:index"))


def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse("assistant:index"))


def account(request):
    if request.method == "GET":
        return render(request, "users/account.html")
    elif request.method == "POST":
        form = request.POST

        username = form["username"]
        password = form["password"]

        user = CustomUser.objects.get(username=username)
        user.set_password(password)
        user.save()

        django_login(request, user)
        return render(request, "users/account.html")
