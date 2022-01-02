from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='home'),
    path('form', views.form, name='form'),
    path('tasklist', views.tasklist, name='tasklist')
]
