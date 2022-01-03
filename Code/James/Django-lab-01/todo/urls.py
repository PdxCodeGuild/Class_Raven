from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    
    path('', views.index, name='home'),
    path('add-todos/', views.save_todo_item, name='add_todos')
]