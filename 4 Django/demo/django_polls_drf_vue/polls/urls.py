from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='home'),
    path('list/', views.polls_list, name="polls_list"),
    path('create/', views.create_question, name='create'),
    path('vote/', views.vote, name='vote'),
    path('polls/<str:username>/', views.user_polls_list, name='user_polls_list'),
]
