from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import (
    authenticate,
    login as django_login
)
from .models import TodoItem
from colorama import Fore as F

R = F.RESET


# Create your views here.

def index(request):

    items = TodoItem.objects.all().order_by('-created_date')

    context = {
        "items": items,
    }

    return render(request, "todo_list/index.html", context)


def create(request):

    if request.method == 'GET':
        return render(request, "todo_list/create.html")

    form = request.POST
    print(form)

    name = form["name"]
    text = form["message"]
    priority = form["priority"]

    todo_item = TodoItem()
    todo_item.todo_name = name
    todo_item.text = text
    todo_item.priority = priority

    todo_item.save()

    # context = {
    #     "message": todo_item,
    #     "priority": priority_item
    # }

    return render(request, "todo_list/create.html")


def update(request):

    if request.method == 'GET':
        items = TodoItem.objects.all()
        context = {
            "items": items
        }
        return render(request, "todo_list/update.html", context)

    form = request.POST
    print(form)


def delete(request):

    if request.method == 'GET':

        items = TodoItem.objects.all()
        context = {
            "items": items
        }
        return render(request, "todo_list/delete.html", context)

    form = request.POST
    print(form)
    todo_item = form["todo-delete"]

    try:
        todo_inst = TodoItem.objects.get(todo_name=todo_item)
        todo_inst.delete()
        print(f"{F.GREEN}Delete successful!{R}")
    except:
        print(f"{F.RED}failed to delete!{R}")

    return render(request, "todo_list/delete.html")


def completed(request):

    if request.method == 'GET':
        return render(request, "todo_list/completed.html")

    form = request.POST
    print(form)


def signup(request):

    if request.method == 'GET':
        
        return render(request, "todo_list/signup.html")
    
    form = request.POST
    username = form["username"]
    password = form["password"]

    user = authenticate(request, username=username, password=password)

    if user is not None:
        django_login(request, user)

        # return redirect(reverse())

    print(form)


def login(request):

    if request.method == 'GET':
        return render(request, "todo_list/login.html")

    form = request.POST
    print(form)


def logout(request):
    return render(request, "todo_list/logout.html")
