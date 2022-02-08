from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('keys/', views.KeyListView.as_view(), name='keys'),
    path('key/<int:pk>', views.KeyDetailView.as_view(), name='key-detail'),
    path('mykeys/', views.LoanedKeysByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', views.LoanedKeysAllListView.as_view(), name='all-borrowed'), 
    path('key/<pk>/renew/', views.renew_key_librarian, name='renew-key-librarian'),
]