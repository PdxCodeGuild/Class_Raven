from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegisterForm


def register(request):
    context = {
        'form': RegisterForm()
    }
        

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            # new_user = form.save(commit=False)
            # new_user.set_password(form.cleaned_data['password'])
            # new_user.save()

            # create a profile for the new user
            # Profile.objects.create(user=new_user)

            new_user = form.save()
            return redirect(reverse('profiles_app:profile', kwargs={'username': new_user.username}))
        else:
            print(form.errors)
    
    return render(request, 'register.html', context)
