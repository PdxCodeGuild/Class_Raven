from django.urls import path, include

from . import views
app_name = 'myapp'

urlpatterns = [
    path('', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('register_user', views.register_user, name='register_user'),
    path('profile/create', views.create, name='create')

]