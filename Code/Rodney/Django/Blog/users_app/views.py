from django.contrib import auth
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import UserAuthForm, UserForm
from django.contrib.auth import (authenticate, get_user_model,
login as django_login,
logout as django_logout )
from django.contrib.auth.decorators import login_required





def register(request):
    ## this is creating an empty form when user lands on page

    form = UserAuthForm()

    if request.method == 'GET':

        context = {
            'form': form
        }

        return render(request, 'users/register.html', context)


    if request.method == 'POST':

        ##creating a UserAuthForm with HTML form data 

        form = UserAuthForm(request.POST)
        
        if form.is_valid():
            ## commit false creates object, doesn't save it
            new_user = form.save(commit=False)
            
            ## after you get form is valid, you get access to cleaned_data dictionary
            new_user.set_password(form.cleaned_data['password'])

            #without this, you would just have a plain text password which won't allow you to log in ?? (I think)


            ## now save the new user object to the database 
            new_user.save()

            ## redirect does same as HTTP Response Redirect, a short cut 

            return redirect(reverse('users_app:login'))

        else:

            context = {

                'form': UserAuthForm(),
                'errors': ['User already exists! Please try again']
            }

            return render (request, 'users/register.html', context)

def login(request):

    if request.method == 'GET':

        form = UserAuthForm()

        context = {
            'form': form
        }

        return render(request, 'users/login.html', context)

    if request.method == 'POST':

        ## get form data from request

        form = request.POST 

        username = form['username']
        password = form['password']

        ## try to authenticate user
        user = authenticate(request, username=username, password=password)

        ## if credentials not valid, return error 
        if user is None:
            context = {
                'form': UserAuthForm(),
                'errors': ['Invalid Username or Password']
            }

            return render(request, 'users/login.html', context)

        else: 

            django_login(request, user)

            # redirect to users profile page
            return redirect(reverse('users_app:userprofile', kwargs={'username': user.username}))

@login_required
def userprofile(request, username):
    # find the user that just logged in
    user = get_object_or_404(get_user_model(), username=username)

    # print(user.blogpost.all())

    return render(request, 'users/userprofile.html', {'user': user})

def logout(request):
    django_logout(request)

    return redirect(reverse('users_app:login'))

