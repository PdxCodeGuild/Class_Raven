from django.urls import path
from . import views as view

app_name = 'USER'
urlpatterns = [
    path('login', view.login.form, name='login'),
    path('auth', view.login.auth, name='auth'),
    path('register', view.login.register, name='register'),
    path('logout', view.login.logout, name='logout'),
    path('view', view.profile.view, name='view'),
]
