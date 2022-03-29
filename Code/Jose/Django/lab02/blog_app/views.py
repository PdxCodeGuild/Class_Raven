from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogForm
# Create your views here.


def home(request):
    blogs = BlogPost.objects.all().order_by("-date_created")
    context = {"blogs": blogs}
    return render(request, "home.html", context)


@login_required
def create(request):
    if request.method == "GET":
        form = BlogForm()
        return render(request, "create.html", {"form": form})

    elif request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.user = request.user
            new_blog.save()

        return redirect(reverse("blog_app:home"))