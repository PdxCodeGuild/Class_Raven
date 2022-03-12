from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from blog_project_app.models import BlogPost
from django.contrib.auth import (
    authenticate,
    login as django_login,
    logout as django_logout
)
from users.models import CustomUser

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

        django_login(request, new_user)
        # return render(request, '/')
        return HttpResponseRedirect(reverse('users:profileview'))


def login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')

    elif request.method == 'POST':
        form = request.POST

        # pull the form information from the form
        username = form['username']
        password = form['password']

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'users/login.html', {'error': 'Invalid Username or Password!'})


        # if the user is authenticated, log them in
        django_login(request, user)

        return HttpResponseRedirect(reverse('users:profileview'))

def logout(request):
    django_logout(request)

    return HttpResponseRedirect(reverse('blog_project_app:index'))

def account(request):
    pass

def profileview(request):
    blogposts= BlogPost.objects.filter(user=request.user)
    
    context = {
        'current_user':request.user, 
        'blogposts': blogposts
    }

    return render(request, 'users/profile.html', context)