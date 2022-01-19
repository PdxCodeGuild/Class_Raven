from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    # add more User fields here
    # Keegan did this, so I do this ¯\_(ツ)_/¯
    pass


    def __str__(self):
        return self.username