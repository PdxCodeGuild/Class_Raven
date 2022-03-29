from django.contrib import admin
from django.urls import path

from todo_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TodoListView.as_view(), name='home.list'),
    #path('<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('index/', views.TodoListView.as_view(), name='index.list'),
    path('todo_form/', views.TodoCreateView.as_view(), name='todo_form.new'),
   # path('details/<int:pk>', views.TodoDetailView.as_view(), name='todo_form.details')
    
]
