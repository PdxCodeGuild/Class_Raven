from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    return render(request, "index.html")

@login_required
def create(request):
    """form for creating a blog post"""


def search(request):
    """form presented to search for a blog"""

@login_required
def edit(request, blog_id):
    """form for editing an existing blog"""

    # blog_post = get_object_or_404()

@login_required
def delete(request):
    """form for deleting a user's blog"""
