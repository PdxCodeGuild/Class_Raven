from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from . import forms
from . import models as model

# Create your views here.

class post:
    def view(REQUEST, username, post_title):
        user = get_object_or_404(get_user_model(), username=username)
        blog = model.Blog.objects.get(user=user)
        selected = model.Post.objects.get(title=post_title)
        context = {
            'posts': model.Post.objects.filter(blog=blog),
            'selected': selected,
            'selected_user': user
        }
        print(context)
        return render(REQUEST, 'blog.html', context)
    def new(REQUEST, username):
        context = {
            'name': 'new post',
            'form': forms.post.new(),
            'url': 'BLOG:new',
            'username': username
        }
        if REQUEST.POST:
            form = forms.post.new(REQUEST.POST, instance=REQUEST.user)
            if form.is_valid():
                blog = model.Blog.objects.get(user=REQUEST.user)
                new_post = form.save(blog=blog)
                
                return redirect(reverse('BLOG:index', kwargs={'username': REQUEST.user.username}))
        return render(REQUEST, 'form.html', context)
    def update(REQUEST, username, post_title):
        selected_post = model.Post.objects.get(title=post_title)
        context = {
            'name': 'edit post',
            'form': forms.post.new(initial={'title': selected_post.title, 'content': selected_post.content}),
            'url': 'BLOG:edit_post',
            'username': username,
            'selected_post': selected_post
        }
        if REQUEST.POST:
            data = REQUEST.POST
            form = forms.post.new(data)
            if form.is_valid():
                form.update(selected_post)
                return redirect(reverse('BLOG:browse'))
        return render(REQUEST, 'form.html', context)
class blog:
    def index(REQUEST, username):
        user = get_object_or_404(get_user_model(), username=username)
        blog = model.Blog.objects.get(user=user)
        context = {
            'posts': model.Post.objects.filter(blog=blog),
            'selected_user': user
        }

        return render(REQUEST, 'blog.html', context)
    def browse(REQUEST):
        context = {
            'blogs': model.Blog.objects.all()
        }
        return render(REQUEST, 'index.html', context)