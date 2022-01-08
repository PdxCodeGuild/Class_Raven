from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login
from .models import User, BlogPost
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    
    return render(request, 'myapp/login.html')

def login_check(request):
    form = request.POST
    username = form['username']
    password = form['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        dj_login(request, user)
        return redirect('myapp:profile')
    else:
        return redirect('myapp:login')

def register(request):
    
    return render(request, 'myapp/register.html')

def register_user(request):
    form = request.POST
    username = form['username']
    password = form['password']

    user = User.objects.create_user(username=username, password=password)
    dj_login(request, user)
    return redirect('myapp:profile')

@login_required
def create(request):
    if request.method == 'POST':
        form = request.POST
        new_title = form['title']
        new_post = form['body']
        new_blog = BlogPost.objects.create(title=new_title, body=new_post, user=request.user)
        return redirect('myapp:profile')

    return render(request, 'myapp/create.html')




@login_required
def profile(request):
    items = BlogPost.objects.filter(user=request.user)
    context = {
        'myitems': items
    }
    return render(request, 'myapp/profile.html', context)
    


    
    


    
