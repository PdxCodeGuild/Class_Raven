from django.urls import path
from . import views


app_name='pokedex'
urlpatterns = [
    path('', views.index, name='index'),
    path('<element_id>', views.select_element, name='select_element')
]