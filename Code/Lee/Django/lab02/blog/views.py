from django.shortcuts import (
    render, # helps render html templates
    get_object_or_404, # returns the desired object if it exists or raises a 404 error
    reverse, # lookup the path associated with a view name
    redirect,
)
from django.http import HttpResponse, HttpResponseRedirect ,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    get_user_model,
)

from .forms import BlogForm
from .models import BlogPost

# Create your views here.
def index(request):

    return render(request, 'users/index.html')


def profile(request, username):

    user = get_object_or_404(get_user_model(), username=username)

    blogs = BlogPost.objects.all().filter(user=user).order_by('-date_created')

    context = {
        'user': user,
        'blogs': blogs
    }

    return render(request, 'blog/profile.html', context)

@login_required
def create(request):
    if request.method == 'GET':
        form = BlogForm
        return render(request, 'blog/create.html', {'form':form})

    elif request.method == 'POST':
        form = BlogForm(request.POST)
        
        if form.is_valid():
            new_blog = form.save(commit=False)
            
            new_blog.user = request.user
            

            new_blog.save()
            print(new_blog)
        return redirect(reverse('blog:profile', kwargs={'username':request.user.username}))