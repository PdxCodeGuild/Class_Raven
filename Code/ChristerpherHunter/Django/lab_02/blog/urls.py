from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('search', views.search, name='search'),
    path('edit/<int:blog_id>', views.edit, name='edit'),
    path('delete/<int:blog_id>', views.delete, name='delete'),
]