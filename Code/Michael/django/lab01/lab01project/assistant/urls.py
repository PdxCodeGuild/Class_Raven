from django.urls import path
from . import views

app_name = "assistant"
urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("todo_list/", views.TodoListListView.as_view(), name="TodoListListView"),
    path("todo_list/<int:pk>/", views.TodoListListView.as_view(), name="TodoListListView"),
    path("task_list/", views.TaskListView.as_view(), name="TaskListView"),
    path("task_list/<int:pk>/", views.TaskListView.as_view(), name="TaskListView"),
    path("task_list/<int:pk>/<int:task_pk>/", views.TaskListView.as_view(), name="TaskListView"),
]
