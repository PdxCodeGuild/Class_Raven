# to match project urls without include
from django.urls import path #include
# import views from views.py for blog_app
from . import views




# include the app name for namespacing the views
app_name = 'blog_app'

urlpatterns = [
# path for register function in views.py 
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'), 
    path('logout/', views.logout, name='logout'),
    path('update/<str:username>/', views.update, name='update'),
    path('<str:username>/', views.detail, name='detail'),


]

