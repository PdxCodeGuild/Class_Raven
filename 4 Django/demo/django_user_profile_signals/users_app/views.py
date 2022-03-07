from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegisterForm

from django.contrib import messages

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
            
            # print(messages.SUCCESS) # 25
            # messages.add_message(request, messages.SUCCESS, f'Welcome, {new_user.username}!')

            # .success() adds the messages.SUCCESS message level integer by default
            messages.success(request, f'Welcome, {new_user.username}!', extra_tags='success')
            messages.warning(request, 'Please check your email!', extra_tags='warning')
            messages.error(request, 'Oops! Something went wrong!', extra_tags='error')

            return redirect(reverse('profiles_app:profile', kwargs={'username': new_user.username}))
        else:
            print(form.errors)
    
    return render(request, 'register.html', context)
