from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import Priority, TodoItem
# Create your views here.

def index(request):
    todos = TodoItem.objects.all().order_by('created_date')
    priority = Priority.objects.all()

    context = {
        'todos': todos,
        'priority': priority,
        'choices': ['high', 'medium', 'low']
    }

    return render(request, 'index.html', context)

def save_todo(request):
    form = request.POST
    text = form['add_todo']

    priority, created = Priority.objects.get_or_create(name = form['key'])
    new_todo = TodoItem()
    new_todo.text = text
    new_todo.priority = priority
    new_todo.save()

    return HttpResponseRedirect(reverse('TodoApp:home'))
