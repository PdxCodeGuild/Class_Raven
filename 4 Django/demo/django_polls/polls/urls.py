from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create_question, name='create'),
    path('add-choices/', views.add_choices, name='add_choices'),
    path('vote/<int:choice_id>', views.vote, name='vote'),
    path('polls/<str:username>/', views.user_polls_list, name='user_polls_list'),
]
