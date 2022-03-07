from django.shortcuts import render

from django.db import connection, reset_queries

from .models import *


def index(request):

    # retrieve only the user objects, not their blogposts or the blogposts' comments
    # 1102 queries to get all the comments
    # users = User.objects.all()

    # retrieve the users and all of their blogposts, but not the comments
    # 101 queries to get all the comments
    # users = User.objects.all().prefetch_related('blogposts')

    # retreive the users, their blogposts and the comments
    # 3 queries to get all the comments
    users = User.objects.all().prefetch_related('blogposts__comments')


    # print(users.blogposts.first().comments.all())

    # for user in users:
    #     # print(user)
    #     for blogpost in user.blogposts.all():
    #         x = blogpost
    #         print(blogpost)
    #         for comment in blogpost.comments.all():
    #             print(comment)
    #             x = comment # evaluate the comment into a variable

    
    query_count = len(connection.queries)
    
    context = {
        'query_count': query_count,
        'users': users
    }

    return render(request, 'index.html', context)
