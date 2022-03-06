from django.urls import path
from .views import *

app_name = 'HOME'
urlpatterns = [
    path('', home, name='page')
]