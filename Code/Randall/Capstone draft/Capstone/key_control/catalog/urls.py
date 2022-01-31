from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('keys/', views.KeyListView.as_view(), name='keys'),
    path('key/<int:pk>', views.KeyDetailView.as_view(), name='key-detail'),
]