from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='home'),
    path('vote/<int:choice_id>', views.vote, name='vote')
]
