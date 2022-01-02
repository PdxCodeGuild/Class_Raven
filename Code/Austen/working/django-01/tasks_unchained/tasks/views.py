from django.shortcuts import render
from django.http import HttpResponse as HTTP
from .models import Task


# Create your views here.
def index(request):
  actions = [
      {'name': 'create another task you\'ll just ignore', 'link': 'form'}, 
      {'name': 'look at the mountain of crap you haven\'t done yet', 'link': 'tasklist'}
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
  print(tasks)
  return render(request, 'tasklist.html', context)