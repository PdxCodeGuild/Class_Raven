from django.shortcuts import render, reverse

from django.http import HttpResponseRedirect
from .models import  Priority, Todoitem

# Create your views here.


def indexView(request):
 # need to reference the polls/views.py from the demo folder
   
   
   
   items = Todoitem.objects.all()
   context = {
      'myitems': items
   }
    
    
    
   return render(request, 'myapp/mytemplate.html', context ) #if i return more than one thing it just displays the whole html code

def add_todo(request):
   form = request.POST
   select_choice = form['choice-field']
   new_todo = form['new-todo']

   new_priority = Priority() #creating a new row for priority
   new_todo_item = Todoitem() #creating a new todo item in the DB
   
   new_priority.name = select_choice
   new_priority.save()

   new_todo_item.text = new_todo
 
   new_todo_item.save() #saving the new rows in the database


   
   return HttpResponseRedirect(reverse('myapp:indexView')) #this just redirects back to the main page
   #to show all the todo items
   
   

   