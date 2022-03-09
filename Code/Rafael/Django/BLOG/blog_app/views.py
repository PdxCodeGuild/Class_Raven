from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse
from django.contrib.auth import  authenticate, login as django_login, logout as django_logout, get_user_model
# from classes in form.py
from .forms import UserForm, UserAuthForm
# request.user login_required allows only logged in users to edit a profile
from django.contrib.auth.decorators import login_required

# Create your views here.
'''
# request object
def register(request):

    form = UserForm()
    #context dictionary
    context = {
        'form': form
    }


    return render(request, 'users/register.html', context)
'''
def register(request):

    form = UserAuthForm()
# If the form is blank it will render
    if request.method =='GET': 
    #context dictionary
        context = {
            'form': form
        }


        return render(request, 'users/register.html', context)

# takes the data from the html form through UserAuthForm
    if request.method == 'POST': 
       #UserAuthForm with the data from the html request
        form = UserAuthForm(data=request.POST)
       # prints the html form in the console; "didn't return an HttpResponse object. Ir returned None instead"
       #print(form)
       # to see the actual values you would print(form.initial)
       # print(form.is_valid()) function to see the boolean if the form is good or not. True is good data. 
       #print(form.is_valid())
       # to get a list of errors you can print using: print(form.errors)

       # if the form is valid when submitted, checks the validity and then saves the form values to the assigned user
    if form.is_valid():
        new_user = form.save(commit=False)
        # New user password to the key of 'password'
        # use square brackets to prevent "dict' object is not callable"
        new_user.set_password(form.cleaned_data['password'])
        # saves new user to the databases
        new_user.save()
          
    # http response and redirect are basically the same thing
        return redirect(reverse('blog_app:register'))

    # creates a list of errors
    else:
        context = {
        'form': UserAuthForm(),
        'errors': form.errors
        } 
        #print(context)
        print(form.errors)

        return render(request, 'users/register.html', context)


#127.0.0.1:8000/users/login
def login(request): 
    #render the form with request.method
    if request.method == 'GET':
        form = UserAuthForm()

        context = {
            'form': form
        }

        return render(request, 'users/login.html', context)

    elif request.method == 'POST': 
        form = request.POST

        username = form['username']
        password = form['password']
        #email = form['email']

    user = authenticate(request, username=username, password=password)
# Error arises if user is None
    if user is None: 
        context = {
            'form': UserAuthForm(),
            'errors': ['Invalid Username or Password']
        }

        return render(request, 'users/login.html', context)

    else: 
        django_login(request, user)

        return redirect(reverse('blog_app:detail', kwargs={'username': user.username}))



def detail(request, username): 
    user = get_object_or_404 (get_user_model(), username=username)
    #context = {'user': user}

    return render(request, 'users/detail.html', {'user':user})

# setting.py LOGIN_URL = '/users/login' redirects to login if not logged in
@login_required
def update(request, username): 
    user = get_object_or_404 (get_user_model(), username=username)

    if request.method == 'GET':
        # displays the current fields for the user in the form (pre-loaded)
        form = UserForm(instance=user)

        #context ={
            #'form':form
       #}
        return render(request, 'users/update.html', {'form':form})

    elif request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        #print(form.initial)
        #print(form.is_valid())
        #print(form.errors)
        #print(request.POST)
        #print(request.FILES)

     #   new_pic = request.FILES.get('avatar')
    #if new_pic:
     #   form.initial['avatar'] = new_pic

    if form.is_valid():
        form.save()

        return redirect(reverse('blog_app:detail', kwargs={'username': user.username}))
    else: 
        errors = [value for value in form.errors.values()]
        context = {'user': user, 'errors': errors}

        return render(request, 'users/update.html', context)

def logout(request): 
    django_logout(request)
    return redirect(reverse('blog_app:login'))


