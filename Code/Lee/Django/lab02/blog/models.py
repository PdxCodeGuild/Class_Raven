from django.db import models
from django.contrib.auth import get_user_model
from users.models import User
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=20000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    public = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True) 
    date_edited = models.DateTimeField(auto_now=True)
# def save(self, args, kwargs) - Look it up on the django site