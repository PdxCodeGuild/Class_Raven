from datetime import datetime
from random import randint
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required


# Index page
def index(request):
    return HttpResponseRedirect(reverse("assistant:view_all_tasks"))


# Creates a task
@login_required
def create_task(request):
    if request.method == "POST":
        try:
            Priority.objects.get(name=int(request.POST["priority"]))
        except:
            Priority.objects.create(name=int(request.POST["priority"]))
        TodoItem(
            name=request.POST["name"],
            description=request.POST["description"],
            owner=request.user,
            priority=Priority.objects.get(name=int(request.POST["priority"])),
        ).save()
        return HttpResponseRedirect(reverse("assistant:view_all_tasks"))
    else:
        return render(request, "assistant/create_task.html")


# Deletes a task
@login_required
def delete_task(request, task_id):
    get_object_or_404(TodoItem, pk=task_id).delete()
    return HttpResponseRedirect(reverse("assistant:view_all_tasks"))


# Shows all tasks
@login_required
def view_all_tasks(request):
    tasks = TodoItem.objects.all()
    return render(request, "assistant/task_list.html", {"tasks": tasks})


# Completes a task
@login_required
def complete_task(request, task_id):
    try:
        Priority.objects.get(name=0)
    except:
        Priority.objects.create(name=0)
    task = get_object_or_404(TodoItem, pk=task_id)
    task.completed = datetime.now()
    task.priority = Priority.objects.get(name=0)
    task.save()
    return HttpResponseRedirect(reverse("assistant:view_all_tasks"))
