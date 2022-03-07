"""Django Lab02 Blog Post
By: Philip Bartoo
1/11/2022

Build a blog using Django.

I used almost all Class based views as this is much quicker to set up CRUD operations than working through function based views.  
The primary thing I learned was the need to build an app along a template first, then to customize later. 
This should allow me to develop apps faster.  I also added a url.py file to the app, which simplified template access that I struggled with in my first Django app.  The other big learning point was setup of
the login function. In this project the login is built into the app.  Alternatively the login could be built as its own app.  I didn't add
a static folder to this app in the interest of time, but will plan to go back and update at a later point in time.  There are several
relatively simple functional improvements which need to be made, such as only showing the logout function when logged in.  I also did not
include a list of all posts, another item I'd really like to update in future revisions. """

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, User
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView



class LoginInterfaceView(LoginView):
    template_name = 'login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('profile')

#def home(request):
    #posts=Post.objects.order_by('-date_created')
    #return render(request,'home.html', {'posts':posts})

class HomeView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_created']
    login_url = "login"

    def get_queryset(self):
        return self.request.user.notes.all()

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'title_tag','body','public')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body', 'public',]

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('profile')