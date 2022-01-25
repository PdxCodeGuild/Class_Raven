from django.urls import path
from . import views


app_name='myapp'
urlpatterns = [
    path('', views.indexView, name='indexView'),
    path('newtodo/', views.add_todo, name='add_todo')

]