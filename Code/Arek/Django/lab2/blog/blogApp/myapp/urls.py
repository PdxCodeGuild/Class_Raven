from django.urls import path, include
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register_page, name='register_page'),
    path('register/new/', views.register, name='register'),
    path('profile/', views.profile, name='profile')
]