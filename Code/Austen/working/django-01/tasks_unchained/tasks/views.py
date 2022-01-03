from django.shortcuts import render
from django.http import HttpResponse as HTTP
from .models import Task


# Create your views here.
def index(request):
  actions = [
      {'name': 'create another task you\'ll just ignore', 'link': 'form'}, 
      {'name': 'look at the mountain of crap you haven\'t done yet', 'link': 'tasklist'},
      {'name': 'admin', 'link': 'admin'},
    ]
  context = {
    'actions': actions
  }
  return render(request, 'index.html', context)

def form(request):
  fields = Task
  context = {
    'fields': fields
  }
  
  return render(request, 'form.html', context)

def tasklist(request):
  tasks = Task.objects.all()
  context = {
    'tasks': tasks
  }
  return render(request, 'tasklist.html', context)

def submit(request):
  submission = request.POST
  task_name = submission['task-name']
  new_task = Task()
  new_task.name = task_name
  new_task.save()
  tasks = Task.objects.all()
  context = {
    'tasks': tasks
  }
  return render(request, 'tasklist.html', context)
  
def update(request):
  form = request.POST
  tasks = Task.objects.all()
  # ? Cannot get tasks to update >:(
  return HTTP('check terminal')