from django.urls import path
from . import views

app_name='blog_project_app'
urlpatterns = [
    path('', views.blogview, name='blogview'),
    path('create/', views.createpostview, name='createpostview')
]