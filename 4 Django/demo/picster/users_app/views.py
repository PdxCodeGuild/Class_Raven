from django.shortcuts import render, redirect, reverse

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
                'errors': form.errors
            }

            return render(request, 'users/register.html', context)