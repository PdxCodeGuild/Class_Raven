from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass # abstract user already has the username and password fields


    def __str__(self):
        return self.username