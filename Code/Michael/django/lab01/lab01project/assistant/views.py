from django.shortcuts import render, get_list_or_404, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from users.models import CustomUser

# Create your views here.


def index(request):
    return render(request, "assistant/index.html")

def add_task(request):
    return render(request, "assistant/add_task.html")

def task_list(request):
    return render(request, "assistant/task_list.html")

def task_detail(request):
    return render(request, "assistant/task_detail.html")

def task_edit(request):
    return render(request, "assistant/task_edit.html")

def task_delete(request):
    return render(request, "assistant/task_delete.html")

def task_complete(request):
    return render(request, "assistant/task_complete.html")

def task_incomplete(request):
    return render(request, "assistant/task_incomplete.html")

def task_add_comment(request):
    return render(request, "assistant/task_add_comment.html")

def task_delete_comment(request):
    return render(request, "assistant/task_delete_comment.html")

def task_edit_comment(request):
    return render(request, "assistant/task_edit_comment.html")

def task_add_subtask(request):
    return render(request, "assistant/task_add_subtask.html")

def task_delete_subtask(request):
    return render(request, "assistant/task_delete_subtask.html")

def task_edit_subtask(request):
    return render(request, "assistant/task_edit_subtask.html")

def task_complete_subtask(request):
    return render(request, "assistant/task_complete_subtask.html")

def task_incomplete_subtask(request):
    return render(request, "assistant/task_incomplete_subtask.html")

def task_add_attachment(request):
    return render(request, "assistant/task_add_attachment.html")

def task_delete_attachment(request):
    return render(request, "assistant/task_delete_attachment.html")

def task_edit_attachment(request):
    return render(request, "assistant/task_edit_attachment.html")

def task_add_tag(request):
    return render(request, "assistant/task_add_tag.html")

def task_delete_tag(request):
    return render(request, "assistant/task_delete_tag.html")

def task_edit_tag(request):
    return render(request, "assistant/task_edit_tag.html")

def task_add_user(request):
    return render(request, "assistant/task_add_user.html")

def task_delete_user(request):
    return render(request, "assistant/task_delete_user.html")

def task_edit_user(request):
    return render(request, "assistant/task_edit_user.html")
