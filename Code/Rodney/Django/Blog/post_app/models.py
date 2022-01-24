from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.fields import BooleanField, TextField

from users_app.models import User


class BlogPost(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_body = models.TextField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')
    public_post = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
