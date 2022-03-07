from django.urls import path

from . import views

app_name = 'profiles_app'
urlpatterns = [
    path('<str:username>/', views.profile, name='profile')
]