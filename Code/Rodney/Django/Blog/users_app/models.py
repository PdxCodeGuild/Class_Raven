from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.fields import BooleanField, TextField


class User(AbstractUser):

    user_blog_name = models.CharField(max_length=200)

    def __str__(self):
        return self.username

