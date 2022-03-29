from django.urls import path
from . import views

# Create your views here.

app_name = 'blog_app'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
]