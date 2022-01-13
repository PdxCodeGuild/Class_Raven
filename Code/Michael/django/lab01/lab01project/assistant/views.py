from django.shortcuts import render, get_list_or_404, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from users.models import CustomUser

# Create your views here.

def index(request):
    return render(request, "assistant/index.html")

def add_task(request):
    return render(request, "assistant/edit_task.html")

def task_list(request):
    return render(request, "assistant/tasks.html")
