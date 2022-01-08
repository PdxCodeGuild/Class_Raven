from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages



#Adds an item to the list 

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item has been added.'))
            return render(request, 'home.html', {'all_items': all_items})

#If nothing is requested to add to list then just show the current list
#=====================SOMETHING WRONG HERE. ERROR WHEN NOTHING POSTED TO ADD======
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item delete'))
    return redirect('home')

