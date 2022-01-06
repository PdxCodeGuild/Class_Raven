from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),   
    path('create/', views.save_todo_item, name='create'),
    path('complete/<int:todo_id>', views.complete_todo_item, name='complete'),
    path('delete/<int:todo_id>', views.delete_todo_item, name='delete')
]

app_name = "todo"