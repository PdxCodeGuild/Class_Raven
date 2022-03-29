from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


app_name = 'post_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]

