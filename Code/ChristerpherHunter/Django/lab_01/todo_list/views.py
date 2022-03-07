from colorama import Fore as F
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.shortcuts import get_object_or_404, redirect, render

from .models import Priority, TodoItem

R = F.RESET


# Create your views here.

def index(request):

    if request.method == 'GET':
        items = TodoItem.objects.all().order_by('-created_date')

        context = {
            "items": items,
        }

        return render(request, "todo_list/index.html", context)


def create(request):

    if request.method == 'GET':
        return render(request, "todo_list/create.html")

    form = request.POST

    name = form["name"]
    text = form["message"]
    priority = form["priority"]

    if name == "":
        return redirect(to="/todo_list")

    todo_item = TodoItem()
    priority_obj = Priority.objects.get_or_create(priority_value=priority)[0]

    todo_item.todo_name = name
    todo_item.text = text

    todo_item.priority = priority_obj

    todo_item.save()

    # updated_info = TodoItem()
    # context = {
    #     "message": updated_info
    # }

    return redirect(to="/todo_list")


def todo_update(request):

    if request.method == 'GET':

        # todo = get_object_or_404(TodoItem, id=todo_id)
        items = TodoItem.objects.all().order_by('-created_date')

        context = {
            "items": items
        }

        return redirect("/todo_list/todo_update.html", context)


def update(request):

    if request.method == 'GET':
        items = TodoItem.objects.all().order_by('-created_date')
        context = {
            "items": items
        }
        return render(request, "todo_list/update.html", context)

    todo = get_object_or_404(TodoItem, id=request.POST["todo-update"])

    return render(request, "todo_list/todo_update.html", {"items": todo})

def delete(request):

    if request.method == 'GET':

        items = TodoItem.objects.all()
        context = {
            "items": items
        }
        return render(request, "todo_list/delete.html", context)

    form = request.POST
    todo_item = form["todo-delete"]

    try:
        todo_inst = TodoItem.objects.get(todo_name=todo_item)
        todo_inst.delete()
        print(f"{F.GREEN}Delete successful!{R}")
    except:
        print(f"{F.RED}failed to delete!{R}")

    items = TodoItem.objects.all()
    context = {
        "items": items
    }

    return render(request, "todo_list/delete.html", context)


def completed(request):

    items = TodoItem.objects.all().order_by('-created_date')
    context = {
        "items": items
    }

    return render(request, "todo_list/completed.html", context)


def toggle_completed(request, todo_id):

    todo = get_object_or_404(TodoItem, id=todo_id)

    todo.completed_or_not = not todo.completed_or_not

    todo.save()

    items = TodoItem.objects.all().order_by('-created_date')
    context = {
        "items": items
    }

    return render(request, "todo_list/index.html", context)


def undo_todo(request, todo_id):

    todo = get_object_or_404(TodoItem, id=todo_id)

    todo.completed_or_not = not todo.completed_or_not

    todo.save()

    items = TodoItem.objects.all().order_by('-created_date')
    context = {
        "items": items
    }

    return render(request, "todo_list/index.html", context)


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
