from django.urls import path
from . import views as view

app_name = 'BLOG'
urlpatterns = [
    path('browse/', view.blog.browse, name='browse'),
    path('<str:username>/new/', view.post.new, name='new'),
    path('<str:username>/posts/', view.blog.index, name='index'),
    path('<str:username>/posts/<str:post_title>/', view.post.view, name='view'),
    path('<str:username>/posts/<str:post_title>/edit', view.post.update, name='edit_post'),
]