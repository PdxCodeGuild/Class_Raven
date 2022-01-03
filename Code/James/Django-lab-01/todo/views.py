from typing import Text
from django.http.response import HttpResponseRedirect
from django.shortcuts import (
    render,
    get_object_or_404,
    reverse
    
    )

from django.http import HttpResponse, Http404

from .models import Priority, Todoitem
# Create your views here.

app_name = 'todo'


def index(request):
    todos = Todoitem.objects.all().order_by('created_date')
    
    priority = Priority.objects.all()
    
    p = Todoitem.objects.get(text = 'Mow the lawn')

    print(p.priority.name)
    
    context = {
        'todos': todos,
        'priority': priority
    }


    return render(request, 'index.html', context)

def save_todo_item(request):
    
    form = request.POST
    
    text = form['add_todo']

    new_todo = Todoitem()
    new_todo.text = text
    new_todo.save()

   
    print(form)
    return HttpResponseRedirect(reverse('todo:home'))
    