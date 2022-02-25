from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms
# Create your views here.
class login:
    def form(REQUEST):
        context = {
            'name': 'login',
            'form': forms.user.login(),
            'url': 'USER:auth'
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
                context.update({'errors': errors})
        return render(REQUEST, 'form.html', context)

    def logout(REQUEST):
        from django.contrib.auth import logout as djlogout
        djlogout(REQUEST)
        return redirect(reverse('USER:login'))
        
class profile:
    def view(REQUEST):
        return render(REQUEST, 'profile.html')