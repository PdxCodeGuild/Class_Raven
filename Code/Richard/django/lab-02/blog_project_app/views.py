from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, request
from .models import BlogPost
from users.models import CustomUser
# Create your views here.

def blogview(request):
    blogposts= BlogPost.objects.all()
    context = {
        'blogposts': blogposts
    }
    return render(request, 'blog_project_app/index.html', context)

def profileview(request):
    blogposts= BlogPost.objects.all()
    
    context = {
        'blogposts': blogposts
    }

    return render(request, 'blog_project_app/profile.html', context)

def createpostview(request):
    context = {
        'message': 'create post here'
    }

    return render(request, 'blog_project_app/create.html', context)

def registerview(request):
    # blogposts= BlogPost.objects.all()
    # context = {
    #     'blogposts': blogposts
    # }
    # return render(request, 'blog_project_app/register.html', context)

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

        return HttpResponseRedirect(reverse('blog_project_app:index'))