from django.shortcuts import render

from datetime import datetime
from django.views.generic import CreateView, ListView

from .models import Todo
 
#Using class based views
#List View for main page
class TodoListView(ListView):
    model = Todo
    context_object_name = "items"
    template_name = "index.html"

#Create item view
class TodoCreateView(CreateView):
    model = Todo
    fields = ['title','priority_choice']
    success_url = '/index'



    
    
    



#Function based views
'''def index(request):
    all_todos = Todo.objects.all() 
    return render(request, 'index.html',{
        'all_todos':all_todos,
    })

def details(request, item_id):
    each_todo = Todo.objects.get(id=item_id)
    return render(request, 'save_todo_item.html', {
        'each_todo':each_todo,
    })

def save_todo_item(request,item_id):
    new_todo = Todo.objects.create()

def todo_detail(request, item_id):
    item = Todo.objects.get(id=item_id)
    return render(request, 'todo_detail.html', {'item':item,})

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title','priority_choice']
    success_url = '/index'

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title','priority_choice','complete','completed_date']
    success_url = '/index'

class TodoDetailView(DetailView):
    model = Todo
    context_object_name = 'todo_detail'
    template_name = 'todo_detail.html'
    '''