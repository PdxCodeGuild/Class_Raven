from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.utils import timezone



#Adds an item to the list 

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item has been added.'))
            return render(request, 'home.html', {'all_items': all_items})


#=====================SOMETHING WRONG HERE. ERROR WHEN NOTHING POSTED TO ADD======
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item delete'))
    return redirect('home')
"""
def created_date(request):
    created_date=timezone.now()

    return render(request, 'home.html', {'created_date': created_date})
"""