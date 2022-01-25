from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth import (
    get_user_model, # returns the AUTH_USER_MODEL variable's value from settings.py
    authenticate,
    login as django_login,
    logout as django_logout
)
from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserAuthForm

def register(request):
    # create a blank form
    form = UserAuthForm()
    if request.method == 'GET':
        context = {
            'form': form
        }

        return render(request, 'users/register.html', context)


    # when the form is submitted, check the validity of the values and 
    # if they are, create a new User object
    if request.method == 'POST':
        # create a UserAuthForm with the data from the HTML form
        form = UserAuthForm(request.POST)

        # print(form.is_valid())
        # print(form.errors)

        if form.is_valid():
            # commit=False will create the object but won't save it
            new_user = form.save(commit=False)

            # set the new user's password
            # validated form data is in form.cleaned_data
            new_user.set_password(form.cleaned_data['password'])

            # save the object to the database
            new_user.save()

            # redirect() does the same thing as HttpResponseRedirect
            return redirect(reverse('users_app:register'))

        else:
            context = {
                'form': UserAuthForm(),
                'errors': [value for value in form.errors.values()]
            }

            return render(request, 'users/register.html', context)


def login(request):
    if request.method == 'GET':
        # blank form
        form = UserAuthForm()
        return render(request, 'users/login.html', {'form': form})

    elif request.method == 'POST':
        # get the form data from the request
        form = request.POST

        username = form['username']
        password = form['password']

        # attempt authentication with the given credentials
        user = authenticate(request, username=username, password=password)

        # if the form credentials are not valid, render the login page with an error
        if user is None:
            context = {
                'form': UserAuthForm(),
                'errors': ['Invalid Username or Password']
            }

            return render(request, 'users/login.html', context)

        else:
            
            # login the user
            django_login(request, user)

            # redirect to the user's detail page
            return redirect(reverse('users_app:detail', kwargs={'username': user.username}))

    
def list_users(request):
    users = get_user_model().objects.all().order_by('username')

    return render(request, 'users/list.html', {'users': users})


def detail(request, username):
    # find the desired user
    user = get_object_or_404(get_user_model(), username=username)
    return render(request, 'users/detail.html', {'user': user})

@login_required
def update(request, username):
    user = get_object_or_404(get_user_model(), username=username)

    if request.method == 'GET':
        # create a UserForm with the current user data
        form = UserForm(instance=user)

        return render(request, 'users/update.html', {'form': form})

    elif request.method == 'POST':
        # create a UserForm with the form data and
        # the User instance to which to apply the changes
        form = UserForm(request.POST, instance=user)
        
        # the file from the form will be within request.FILES 
        # add the filename to the initial form data
        new_avatar = request.FILES.get('avatar')

        # if a file was uploaded, add it to the form
        if new_avatar:
            form.initial['avatar'] = new_avatar

        if form.is_valid():
            # update the user instance with the new data
            form.save()

            # redirect to the user's detail page
            return redirect(reverse('users_app:detail', kwargs={'username': user.username}))

        else:
            errors = [value for value in form.errors.values()]
            context = {
                'user': user,
                'errors': errors
            }

            return render(request, 'users/update.html', context)

def logout(request):
    django_logout(request)

    return redirect(reverse('users_app:login'))


@login_required
def follow(request, user_id):
    # get the user to be followed from the db
    user = get_object_or_404(get_user_model(), id=user_id)

    # if they aren't already in the list of followers,
    # add the user who made the request to the followers list
    # of the user from the db. If they are in the list, remove them (unfollow)
    if request.user not in user.followers.all():
        user.followers.add(request.user)

    else:
        user.followers.remove(request.user)

    return JsonResponse({
        'isFollowing': request.user in user.followers.all(),
        'followerCount': user.followers.count(),
        'followingCount': request.user.following.count(),
        'followerId': request.user.id
    })