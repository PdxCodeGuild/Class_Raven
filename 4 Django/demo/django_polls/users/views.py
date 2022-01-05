from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout
)
from users.models import CustomUser


# when register/ is visited with a GET request, the form will load
# when register/ is visited with a POST request, the form will be processed
def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')

    elif request.method == 'POST':
        form = request.POST

        username = form['username']
        password = form['password']
        email = form['email']
        first_name = form['first-name']
        last_name = form['last-name']

        print(username, password, email, first_name, last_name)

        # create a new user with the form data
        new_user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        # alternative is to use .create() and set the password after
        # new_user.set_password(password)
        # new_user.save()
        # log the user in by default
        django_login(request, new_user)

        return HttpResponseRedirect(reverse('polls:home'))


def login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')

    elif request.method == 'POST':
        form = request.POST

        # pull the form information from the form
        username = form['username']
        password = form['password']

        # try to authenticate the user with the credentials from the form
        # authenticate() returns either the user, if authenticated or None
        user = authenticate(request, username=username, password=password)

        # if the user is not authenticated, render the login form with an error
        if user is None:
            return render(request, 'users/login.html', {'error': 'Invalid Username or Password!'})


        # if the user is authenticated, log them in
        django_login(request, user)

        return HttpResponseRedirect(reverse('polls:home'))

def logout(request):
    django_logout(request)

    return HttpResponseRedirect(reverse('polls:home'))

def account(request):
    pass