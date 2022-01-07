from django.urls import path
from . import views

app_name = "todo_list"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("update/", views.update, name="update"),
    path("todo_update/", views.todo_update, name="todo_update"),
    path("delete/", views.delete, name="delete"),
    path("completed/", views.completed, name="completed"),
    path("toggle_completed/<int:todo_id>", views.toggle_completed, name="toggle_completed"),
    path("undo_todo/<int:todo_id>", views.undo_todo, name="undo_todo"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name ="signup"),
]
