from django.urls import path
from pokedex_app import views


urlpatterns = [
 
    path('', views.listview, name="home"),
    path('profile/', views.listview, name="profile"),
    path('random/', views.randomview, name="random"),
  
    
] 
