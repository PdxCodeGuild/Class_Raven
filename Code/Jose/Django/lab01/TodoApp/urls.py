from django.urls import path
from . import views

app_name ='TodoApp'
urlpatterns = [
    path('', views.index, name='home'),
    path('add-todo/', views.save_todo, name='add_todos')
]