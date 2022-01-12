from django.shortcuts import render
from django.http import HttpResponse as HTTP
from .models import Task


# Create your views here.
def index(request):
    actions = [
        {'name': 'create another task you\'ll just ignore', 'link': 'form'},
        {'name': 'look at the mountain of crap you haven\'t done', 'link': 'tasklist'},
    ]
    context = {
        'actions': actions
    }
    return render(request, 'index.html', context)


def form(request):
    fields = Task
    context = {
        'fields': fields
    }

    return render(request, 'form.html', context)


def context():
    tasks = Task.objects.all()
    tasks = {
        'tasks': tasks
    }
    return tasks


def tasklist(request):

    return render(request, 'tasklist.html', context=context())


def submit(request):
    submission = request.POST
    task_name = submission['task-name']
    new_task = Task()
    new_task.name = task_name
    new_task.save()

    return render(request, 'tasklist.html', context=context())


def update(request):
    updates = request.POST.getlist(key='task_id')
    tasklist = Task.objects.filter(id__in=updates)
    for task in tasklist:
        task.status = True
        task.save()

    return render(request, 'tasklist.html', context=context())


def update_complete(request):
    do_not_update = request.POST.getlist(key='task_id')
    do_not_update = Task.objects.filter(id__in=do_not_update)
    tasklist = Task.objects.filter(status=True)
    for task in tasklist:
        if task not in do_not_update:
            task.status = False
            task.save()

    return render(request, 'tasklist.html', context=context())


def delete(request):
    if request.method == 'POST':
        delete_us = request.POST.getlist(key='delete_task_id')
        delete_us = Task.objects.filter(id__in=delete_us)
        for task in delete_us:
            task.delete()
        return render(request, 'tasklist.html', context=context())
    return render(request, 'delete.html', context=context())
