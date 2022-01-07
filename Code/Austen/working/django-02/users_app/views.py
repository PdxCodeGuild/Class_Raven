from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse as HTTP
from django.contrib import messages as msg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as auth
from .forms import LoginForm, RegisterForm

# Create your views here.


def login(request):
    form = LoginForm()
    # redirectmsg = msg.get_messages(request)
    if request.method == 'POST':
        form = request.POST
        user = auth(username=form['username'], password=form['password'])
        return render(request, 'login.html', {'logged_in': user})

    return render(request, 'login.html', {'form': form})
    # return render(request, 'login.html', {'form': form, 'messages': redirectmsg})


def register(request):
    form = RegisterForm()
    errors = []
    print(request.method)
    if request.method == 'POST':

        form = request.POST
        username = form['username']
        first = form['first_name']
        last = form['last_name']
        email = form['email']
        if form['password'] == form['confirm']:
            password = form['password']
            user = User.objects.create_user(username, email, password)
            user.first_name = first
            user.last_name = last
            user.save()
            # msg.add_message(request, msg.SUCCESS,
            #                 'account created successfully')
            # form = LoginForm()
            # return render(request, 'login.html', {'form': form, 'success': })
            return redirect(reverse('users:login'))
        else:
            error = 'passwords need to match'
            errors.append(error)
            return render(request, 'register.html', {'registered': error})

    return render(request, 'register.html', {'form': form})
