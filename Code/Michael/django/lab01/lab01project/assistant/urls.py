from django.urls import path
from . import views

app_name = "assistant"
urlpatterns = [
    path("", views.index, name="home"),
]
