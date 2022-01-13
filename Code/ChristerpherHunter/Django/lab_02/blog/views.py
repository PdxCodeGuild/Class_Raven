from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

import users_handler

# Create your views here.


def index(request):

    posts = [
        ("Hey I think that meeting got scheduled for the wrong time because my availability on Calendly ends at 2pm. I canceled that meeting but I have you in my  calendar for 4:30PST tomorrow. We'll use the class call", "Keegan Good"),
        ("My new OS vscode did not sync my key bindings.  Did you happen to copy that editor.emmet.action.wrapWithAbbreviation json config snippet I showed you?", "Christerpher Hunter")
    ]

    
    
    return render(request, "index.html", {"posts": posts})


# @login_required
def create(request):
    """form for creating a blog post"""


def search(request):
    """form presented to search for a blog"""


# @login_required
def edit(request, blog_id):
    """form for editing an existing blog"""

    # blog_post = get_object_or_404()


# @login_required
def delete(request, blog_id):
    """form for deleting a user's blog"""
