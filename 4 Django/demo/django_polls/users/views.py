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

        # create a new user with the form data
        new_user = CustomUser.objects.create(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
        )

        # log the user in by default
        django_login(request, new_user)

        return HttpResponseRedirect(reverse('polls:home'))
