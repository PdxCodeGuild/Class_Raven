from django.urls import path
from . import views

app_name = 'todo_app'
urlpatterns = [
    path('', views.todo_view, name='todo_view'),
    path('create/', views.create_todo, name='create')
]