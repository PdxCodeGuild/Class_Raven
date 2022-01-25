from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='home'),
    path('form', views.form, name='form'),
    path('tasklist', views.tasklist, name='tasklist'),
    path('submit-task', views.submit, name='submit'),
    path('update-list', views.update, name='update'),
    path('update-complete', views.update_complete, name='update_complete'),
    path('delete', views.delete, name='delete')
]
