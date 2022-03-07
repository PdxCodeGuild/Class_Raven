from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
import datetime

# Create your views here.

from django.http import HttpResponse
from .models import TodoItem, Priority


def index(request):
    to_do_list = TodoItem.objects.filter(completed_date__isnull=True)
    completed_to_do_list = TodoItem.objects.filter(completed_date__isnull=False)
    context = {'to_do_list': to_do_list, 'completed_to_do_list': completed_to_do_list}
    return render(request, 'todoapp/index.html', context)

def create(request):
    priority = Priority.objects.get_or_create(priority_level=request.POST['priority_choices'])
    priority = priority[0]
    new_to_do_item = request.POST['todotext']
    new_obj = TodoItem.objects.get_or_create(item_text=new_to_do_item, priority=priority)
    return HttpResponseRedirect("http://127.0.0.1:8000/todoapp/")


def complete(request, pk):
    completed_item = get_object_or_404(TodoItem, pk=pk)
    completed_item.delete()
    priority = completed_item.priority
    print(priority.todoitem_set.all())
    completed_date = datetime.datetime.now()
    new_obj= TodoItem.objects.get_or_create(item_text=completed_item, completed_date=completed_date, priority=priority)
    return HttpResponseRedirect("http://127.0.0.1:8000/todoapp/")
    
def delete(request, pk):
    deleted_item = get_object_or_404(TodoItem, pk=pk)
    deleted_item.delete()
    return HttpResponseRedirect("http://127.0.0.1:8000/todoapp/")
