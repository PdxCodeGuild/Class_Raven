from django.urls import path
from . import views

app_name = "assistant"
urlpatterns = [
    path("index/", views.index, name="index"),  # TODO: Change to landing page
    path("new/", views.create_task, name="create_task"),
    path("", views.view_all_tasks, name="view_all_tasks"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("complete/<int:task_id>/", views.complete_task, name="complete_task"),
]
