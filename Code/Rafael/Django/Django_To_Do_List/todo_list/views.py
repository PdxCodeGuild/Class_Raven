from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import MyModel, Priority
from .forms import MyModelForm


def home(request):
    if request.method == "POST":
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
          
            myinstances = MyModel.objects.all
            return render(request, 'home.html', {'myinstances': myinstances})    
    else:
        if request.method == "POST":
            priority = Priority(request.POST)
            if priority.is_valid():
                priority.save()
        print(Priority._meta.fields[1].choices)
        myinstances = MyModel.objects.all
        return render(request, 'home.html', {'myinstances': myinstances})
    


def priority(request, item_id):
    priority = request.POST.get('priority')
    priority = Priority.objects.get_or_create(priority=priority)
    MyModel.objects.create(mymodel=mymodel, priority=priority)
    myinstances = MyModel.objects.all
    context = {'form': myinstances}
    return redirect(reverse,'todo_list:home', context)
    
    #return redirect('home')            
"""
def priority(request, item_id):
    priority = Priority.objects.all()
    priority = priority
    priority.save()
    mymodel.priority = True
    mymodel.priority = priority
    mymodel.save()
    myinstances = MyModel.objects.all
    context = {'myinstances': myinstances}
    return render(request,'home', context)
    
    #return redirect('home')
"""

def created(request):
    mymodel = Priority()
    #priority = priority() #undefined?
    mymodel.text = request.POST['mymodel']
    mymodel.priority = priority['priority']
    priority.save()
    #print(request.POST)
    #print(Priority._meta.fields[1].choices)
    #print('priorities')
    myinstances = Priority.objects.all
    context = {'myinstances' : myinstances,
    'priority': priority}
    return render(request, 'home', context)

def delete(request, item_id):
    mymodel = MyModel.objects.get(pk=item_id)
    mymodel.delete()
    return redirect('home')

def cross_off(request, item_id):
    mymodel = MyModel.objects.get(pk=item_id)
    mymodel.completed = True
    mymodel.save()
    return redirect('home')

def uncross(request, item_id):
    mymodel = MyModel.objects.get(pk=item_id)
    mymodel.completed = False
    mymodel.save()
    return redirect('home')

