from django.urls import path
from django.urls.resolvers import URLPattern


from . import views


app_name = 'users_app'

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('<str:username>/', views.profile, name='profile')
]