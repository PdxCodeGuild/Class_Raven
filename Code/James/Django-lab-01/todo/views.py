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
    print(priority)

    context = {
        'todos': todos,
        'priority': priority,
        'choices': ['high', 'medium', 'low']
    }

    return render(request, 'index.html', context)


def save_todo_item(request):

    form = request.POST

    text = form['add_todo']
    name = form['key']
    # print(name)
    # priority = Priority.objects.get_or_create(name=form['key'])
    priority, created = Priority.objects.get_or_create(name=form['key'])
    new_todo = Todoitem()
    new_todo.text = text

    new_todo.priority = priority

    new_todo.save()
    return HttpResponseRedirect(reverse('todo:home'))
