from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Priority, TodoItem

# Create your views here.


def todo_view(request):
    todo_instances = TodoItem.objects.all()
    priority_instances = Priority.objects.all()

    context = {
        'todo_instances': todo_instances,
        'priority_instances': priority_instances
    }
    return render(request, 'todo_app/home.html', context)

# everything worked with the quickstart until the below code tried to capture/save the form data.

def create_todo(request):
    # print(request.POST)
    todo_item_text = request.POST['todo_item_text']
    priority_name = request.POST['priority']
    priority = Priority.objects.get_or_create(name=priority_name)[0]
    todo_item = TodoItem(todo_item_text=todo_item_text, priority= priority)
    # priority= Priority.objects.get(name=priority)
    # print(priority_status)
    todo_item.save()
    # priority_status.save()
    # return HttpResponse('form recieved')
    return HttpResponseRedirect(reverse('todo_app:todo_view'))

# (reverse('todo_app:todo_view'))