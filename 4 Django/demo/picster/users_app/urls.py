from django.urls import path

from . import views

app_name = 'users_app'
urlpatterns = [
    path('', views.list_users, name='list_users'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/<str:username>/', views.update, name='update'),
    path('follow/<int:user_id>', views.follow, name='follow'),
    path('<str:username>/', views.detail, name='detail'),
]