from django.shortcuts import render, get_list_or_404, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from users.models import CustomUser as User
from .models import TodoList, Task
from django.contrib.auth.decorators import login_required




# Create your views here.

def index(request):
    return render(request, 'assistant/index.html')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return HttpResponseRedirect(reverse('assistant:task_detail', args=(task.id,)))
    return render(request, 'assistant/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('assistant:todolist_detail', args=(task.todolist.id,)))

def create_task(request, todolist_id):
    todolist = get_object_or_404(TodoList, pk=todolist_id)
    if request.method == "POST":
        task = Task(title=request.POST['title'], description=request.POST['description'], todolist=todolist)
        task.save()
        return HttpResponseRedirect(reverse('assistant:todolist_detail', args=(todolist.id,)))
    return render(request, 'assistant/create_task.html', {'todolist': todolist})

@login_required
def create_todolist(request):
    if request.method == "POST":
        todolist = TodoList(title=request.POST['title'], description=request.POST['description'])
        todolist.save()
        return HttpResponseRedirect(reverse('assistant:todolist_detail', args=(todolist.id,)))
    return render(request, 'assistant/create_todolist.html')

def edit_todolist(request, todolist_id):
    todolist = get_object_or_404(TodoList, pk=todolist_id)
    if request.method == "POST":
        todolist.title = request.POST['title']
        todolist.description = request.POST['description']
        todolist.save()
        return HttpResponseRedirect(reverse('assistant:todolist_detail', args=(todolist.id,)))
    return render(request, 'assistant/edit_todolist.html', {'todolist': todolist})

def delete_todolist(request, todolist_id):
    todolist = get_object_or_404(TodoList, pk=todolist_id)
    todolist.delete()
    return HttpResponseRedirect(reverse('assistant:index'))