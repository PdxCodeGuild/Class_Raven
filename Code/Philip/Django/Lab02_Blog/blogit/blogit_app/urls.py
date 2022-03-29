
from django.urls import path
from . import views
from .views import ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, LoginInterfaceView, LogoutInterfaceView, SignupView, HomeView

urlpatterns = [
 
    path('', HomeView.as_view(), name="home"),
    path('profile',HomeView.as_view(), name="profile"),
    path('post/<int:pk>', ArticleDetailView.as_view(), name='post_detail'), 
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/<int:pk>/edit', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('login', LoginInterfaceView.as_view(), name='login'),
    path('logout', LogoutInterfaceView.as_view(), name='logout'),
    path('register', SignupView.as_view(), name='register'),
    ]
