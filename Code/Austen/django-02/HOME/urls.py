from django.urls import path
from . import views as view
app_name = 'HOME'
urlpatterns = [
    path('', view.home, name='index')
]