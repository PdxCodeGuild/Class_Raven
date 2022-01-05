from django.shortcuts import render, reverse, redirect

from django.http import HttpResponseRedirect
from .models import  Priority, Todoitem


def indexView(request):

   items = Todoitem.objects.all()
   context = {
      'myitems': items
   }
    
   return render(request, 'myapp/mytemplate.html', context ) 

def add_todo(request):
   form = request.POST
   select_choice = form['choice-field']
   new_todo = form['new-todo']

   new_priority,created = Priority.objects.get_or_create(name=select_choice) #creating a new row for priority
   # we put ,created next to new_priority, so that we only get the first part of the tuple
   #.create also does .save() for you
   #.get or create returns a tuple (obj, created=boolean)
   new_todo_item = Todoitem.objects.create(text=new_todo, priority=new_priority)

   return redirect('myapp:indexView') #this just redirects back to the main page
   #to show all the todo items
   # instead of Http response redirect you can just import redirect with django shortcuts
   
   

   