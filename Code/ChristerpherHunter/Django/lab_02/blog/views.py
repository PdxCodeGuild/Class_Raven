from hashlib import new
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost
from django.urls import reverse

# Create your views here.


def index(request):

    all_posts = BlogPost.objects.all()
    return render(request, "index.html", {"posts": all_posts})


@login_required
def create(request):
    """form for creating a blog post"""
    
    if request.method == 'GET':
        return render(request, "create.html")
    
    form = request.POST
    
    new_post = BlogPost()
    new_post.user = request.user
    new_post.title = form["title"]
    new_post.body = form["content"]
    new_post.save()

    return redirect(reverse("users_handler:profile"))

def search(request):
    """form presented to search for a blog"""


# @login_required
def edit(request, blog_id):
    """form for editing an existing blog"""

    # blog_post = get_object_or_404()


# @login_required
def delete(request, blog_id):
    """form for deleting a user's blog"""

    blog = get_object_or_404(BlogPost, id=blog_id)
    blog.delete()

    return redirect(reverse('users_handler:profile'))
