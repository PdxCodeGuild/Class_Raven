from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.db.models.functions import Now

#from Class_Raven.Code.Lee.Django.lab01 import todo

from .models import Priority, TodoItem

# Create your views here.

def index(request):
    all_todo_items = TodoItem.objects.all().order_by('-id')

    context = {
        'all_todo_items': all_todo_items
    }
    return render(request, 'index.html', context) 

def save_todo_item(request):
    form = request.POST

    todo_text = form['todo_text']
    todo_priority = form['todo_priority']
    
    todo_priority, create = Priority.objects.get_or_create(priority=todo_priority)
    TodoItem.objects.create(todo_text=todo_text, todo_priority=todo_priority)    

    all_todo_items = TodoItem.objects.all().order_by('-id')

    context = {
        'all_todo_items': all_todo_items
    }

    return render(request, 'index.html', context)

def complete_todo_item(request, todo_id):

    # Get todo_item
    todo_item = get_object_or_404(TodoItem, id=todo_id)

    # Set completed_date field to time Now
    todo_item.completed_date = Now()

    # Save the item
    todo_item.save()

    # Re-render page with below
    all_todo_items = TodoItem.objects.all().order_by('-id')
    context = {
        'all_todo_items': all_todo_items
    }
    return render(request, 'index.html', context) 

def delete_todo_item(request, todo_id):
    
    # Get todo_item
    todo_item = get_object_or_404(TodoItem, id=todo_id)

    # Delete todo_item from db
    todo_item.delete()

    
    # Re-render page with below
    all_todo_items = TodoItem.objects.all().order_by('-id')
    context = {
        'all_todo_items': all_todo_items
    }
    return render(request, 'index.html', context) 