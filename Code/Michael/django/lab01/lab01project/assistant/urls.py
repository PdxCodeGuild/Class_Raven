from django.urls import path
from . import views

app_name = "assistant"
urlpatterns = [
    path("", views.index.as_view(), name="index"), # TODO: Change to landing page
    path("todo_list/", views.TodoListListView.as_view(), name="TodoListListView"),
    path("todo_list/<int:pk>/", views.TodoListListView.as_view(), name="TodoListListView"),
    path("task_list/", views.TaskListView.as_view(), name="TaskListView"),
    path("task_list/<int:pk>/", views.TaskListView.as_view(), name="TaskListView"),
    path("task_list/<int:pk>/<int:task_pk>/", views.TaskListView.as_view(), name="TaskListView"),
    path("task/<int:pk>/", views.TaskDetailView.as_view(), name="TaskDetailView"),
    path("task/<int:pk>/<int:task_pk>/", views.TaskDetailView.as_view(), name="TaskDetailView"),
    path("todo_list/<int:pk>/task/", views.TaskCreateView.as_view(), name="TaskCreateView"),
    path("todo_list/<int:pk>/task/<int:task_pk>/", views.TaskCreateView.as_view(), name="TaskCreateView"),
    # Create a new todo list
    path("todo_list/new/<int:pk>", views.TodoListCreateView.as_view(), name="TodoListCreateView"),
]
