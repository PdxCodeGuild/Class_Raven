from django.contrib import auth
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponse

from django.contrib.auth import (authenticate, get_user_model,
login as django_login,
logout as django_logout )
from django.contrib.auth.decorators import login_required
from.forms import BlogPostForm
from .models import BlogPost, User



def home(request):
    public_blog_posts = BlogPost.objects.filter(public_post=True).order_by('-created_date')
   
    context = {
        'blogposts': public_blog_posts
    }

    # for blogpost in public_blog_posts:

    #     print(blogpost.blog_title)

    return render(request, 'post/home.html', context)


@login_required
def create(request):

    if request.method == "GET":

        form = BlogPostForm()
        context = {
            'form': form
        }
    
        return render(request, 'post/create.html', context)

    elif request.method == "POST":

        form = BlogPostForm(request.POST)

        if form.is_valid():

            new_post = form.save(commit = False)
            
            ## connect the new post with the user (foreign key)
            new_post.user = request.user
            
            new_post.save()

            return redirect(reverse('post_app:home'))


@login_required
def delete(request, pk):
    deleted_item = get_object_or_404(BlogPost, pk=pk)
    deleted_item.delete()
  
    return redirect(reverse('post_app:home'))
