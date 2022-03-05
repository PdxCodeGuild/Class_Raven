from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import get_user_model, get_user
from . import forms
# Create your views here.
class login:
    def form(REQUEST):
        context = {
            'name': 'login',
            'form': forms.user.login(),
            'url': 'USER:auth',
        }
        return render(REQUEST, 'form.html', context)
    
    def auth(REQUEST):
        from django.contrib.auth import (authenticate as djauth, login as djlogin)
        # print(REQUEST)
        if REQUEST.POST:
            from _project.utils import extract
            form = REQUEST.POST
            errors = []
            keys = ['username', 'password']
            data = extract.request_data(keys, form, return_list=True)
            user = djauth(
                REQUEST, username=data[0], password=data[1]
                )
            if user != None:
                djlogin(REQUEST, user)
                return redirect(reverse('USER:view'))
            else:
                errors.append('invalid login')
                context = {
                    'name': 'login',
                    'form': forms.user.login(),
                    'url': 'USER:auth', 
                    'errors': errors
                }
                return render(REQUEST, 'form.html', context)

    def register(REQUEST):
        context = {
            'name': 'register',
            'form': forms.user.register(),
            'url': 'USER:register'
        }
        if REQUEST.POST:
            form = forms.user.register(REQUEST.POST)
            errors = []
            if form.is_valid():
                form.save()
                return redirect(reverse('USER:login'))
            else:
                errors.append(form.errors.as_text())
                print(errors)
                context.update({'errors': errors})
        return render(REQUEST, 'form.html', context)

    def logout(REQUEST):
        from django.contrib.auth import logout as djlogout
        djlogout(REQUEST)
        return redirect(reverse('USER:login'))
    
    def update(REQUEST):
        form = forms.user.update.password()
        context = {
            'name': 'update password',
            'form': form,
            'url': 'USER:update_password'
        }
        if REQUEST.POST:
            data = REQUEST.POST
            form = forms.user.update.password(data)
            if form.is_valid():
                new_password = form.cleaned_data['password']
                user = get_user(REQUEST)
                user.set_password(new_password)
                user.save()
                return redirect(reverse('USER:login'))
        return render(REQUEST, 'form.html', context)

class profile:
    def view(REQUEST):
        return render(REQUEST, 'profile.html')
    
    def update(REQUEST):
        form = forms.user.update.email()
        context = {
            'name': 'update email',
            'form': form,
            'url': 'USER:update_email'
        }
        if REQUEST.POST:
            data = REQUEST.POST
            form = form(data)
            if form.is_valid():
                user = get_user(REQUEST)
                user.email = data['email']
                user.save()
                return redirect(reverse('USER:view'))
            else:
                context.update({'errors': form.errors.as_text()})
        return render(REQUEST, 'form.html', context)