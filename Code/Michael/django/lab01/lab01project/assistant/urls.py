from django.urls import path
from . import views

app_name = "assistant"
urlpatterns = [
    path("", views.index, name="index"), # TODO: Change to landing page
    #path("todolist/<int:todolist_id>/", views.todolist_detail, name="todolist_detail"),
    path("todolist/new/", views.create_todolist, name="create_todolist"),
]
