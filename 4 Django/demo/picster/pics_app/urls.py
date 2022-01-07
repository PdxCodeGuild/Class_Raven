from django.urls import path

from . import views

app_name='pics_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('update/<int:pic_id>', views.update, name='update'),
    path('pics/<int:pic_id>', views.detail, name='detail'),
    path('delete/<int:pic_id>', views.delete, name='delete'),
    path('like/<int:pic_id>', views.like, name='like'),
]