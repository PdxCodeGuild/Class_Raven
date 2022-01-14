from django.shortcuts import render, get_list_or_404, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.base import TemplateView
from users.models import CustomUser

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TodoList, Task, Comment, Tag, Attachment

# Create your views here.
class TodoListListView(ListView):
    model = TodoList
    template_name = "assistant/todo_list.html"
    context_object_name = "todo_lists"
    
    def get_queryset(self):
        return TodoList.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_lists"] = TodoList.objects.filter(owner=self.request.user)
        return context
    
class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "assistant/todo_list.html"
    context_object_name = "todo_list"
    
    def get_queryset(self):
        return TodoList.objects.filter(owner=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = get_object_or_404(TodoList, id=self.kwargs["pk"])
        return context


class TaskListView(ListView):
    model = Task
    template_name = "assistant/task_list.html"
    context_object_name = "tasks"
    
    def get_queryset(self):
        return Task.objects.filter(todo_list=self.kwargs["pk"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = get_object_or_404(TodoList, id=self.kwargs["pk"])
        return context
    
class TaskDetailView(DetailView):
    model = Task
    template_name = "assistant/task.html"
    context_object_name = "task"
    
    def get_queryset(self):
        return Task.objects.filter(todo_list=self.kwargs["pk"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = get_object_or_404(TodoList, id=self.kwargs["pk"])
        return context


class TaskCreateView(CreateView):
    model = Task
    template_name = "assistant/task_form.html"
    fields = ["name", "due_on", "status", "comment", "tag", "attachment"]
    
    def get_success_url(self):
        return reverse("assistant:task_list", kwargs={"pk": self.kwargs["pk"]})
    
    def form_valid(self, form):
        form.instance.todo_list = get_object_or_404(TodoList, id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = get_object_or_404(TodoList, id=self.kwargs["pk"])
        return context


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "assistant/task_form.html"
    fields = ["name", "due_on", "status", "comment", "tag", "attachment"]
    
    def get_success_url(self):
        return reverse("assistant:task_list", kwargs={"pk": self.kwargs["pk"]})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = get_object_or_404(TodoList, id=self.kwargs["pk"])
        return context
    
    
class TaskDeleteView(DeleteView):
    model = Task
    template_name = "assistant/task_confirm_delete.html"
    
    def get_success_url(self):
        return reverse("assistant:task_list", kwargs={"pk": self.kwargs["pk"]})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = get_object_or_404(TodoList, id=self.kwargs["pk"])
        return context
    
    
class CommentCreateView(CreateView):
    model = Comment
    template_name = "assistant/comment_form.html"
    fields = ["text"]
    
    def get_success_url(self):
        return reverse("assistant:task_detail", kwargs={"pk": self.kwargs["pk"]})
    
    def form_valid(self, form):
        form.instance.task = get_object_or_404(Task, id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, id=self.kwargs["pk"])
        return context
    
    
class CommentUpdateView(UpdateView):
    model = Comment
    template_name = "assistant/comment_form.html"
    fields = ["text"]
    
    def get_success_url(self):
        return reverse("assistant:task_detail", kwargs={"pk": self.kwargs["pk"]})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, id=self.kwargs["pk"])
        return context
    
    
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "assistant/comment_confirm_delete.html"
    
    def get_success_url(self):
        return reverse("assistant:task_detail", kwargs={"pk": self.kwargs["pk"]})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, id=self.kwargs["pk"])
        return context
    

    
class TagCreateView(CreateView):
    model = Tag
    template_name = "assistant/tag_form.html"
    fields = ["name"]
    
    def get_success_url(self):
        return reverse("assistant:task_list", kwargs={"pk": self.kwargs["pk"]})
    
    def form_valid(self, form):
        form.instance.todo_list = get_object_or_404(TodoList, id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = get_object_or_404(TodoList, id=self.kwargs["pk"])
        return context
    
    
class TagUpdateView(UpdateView):
    model = Tag
    template_name = "assistant/tag_form.html"
    fields = ["name"]
    
    def get_success_url(self):
        return reverse("assistant:task_list", kwargs={"pk": self.kwargs["pk"]})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = get_object_or_404(TodoList, id=self.kwargs["pk"])
        return context
    


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "assistant/tag_confirm_delete.html"
    
    def get_success_url(self):
        return reverse("assistant:task_list", kwargs={"pk": self.kwargs["pk"]})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = get_object_or_404(TodoList, id=self.kwargs["pk"])
        return context
    


class AttachmentCreateView(CreateView):
    model = Attachment
    template_name = "assistant/attachment_form.html"
    fields = ["file"]
    
    def get_success_url(self):
        return reverse("assistant:task_detail", kwargs={"pk": self.kwargs["pk"]})
    
    def form_valid(self, form):
        form.instance.task = get_object_or_404(Task, id=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, id=self.kwargs["pk"])
        return context


class AttachmentUpdateView(UpdateView):
    model = Attachment
    template_name = "assistant/attachment_form.html"
    fields = ["file"]
    
    def get_success_url(self):
        return reverse("assistant:task_detail", kwargs={"pk": self.kwargs["pk"]})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, id=self.kwargs["pk"])
        return context


class AttachmentDeleteView(DeleteView):
    model = Attachment
    template_name = "assistant/attachment_confirm_delete.html"
    
    def get_success_url(self):
        return reverse("assistant:task_detail", kwargs={"pk": self.kwargs["pk"]})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, id=self.kwargs["pk"])
        return context
    
class index(TemplateView):
    template_name = "assistant/index.html"