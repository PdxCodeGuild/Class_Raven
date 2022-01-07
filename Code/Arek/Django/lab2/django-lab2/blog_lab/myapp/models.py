from django.db import models
from django.contrib.auth.models import AbstractUser  

# Create your models here.

class User(AbstractUser): #in order to migrate this successfully, do not migrate before this is create like in the django quickstart
    pass # since abstract already has the fields that we need, we dont need to specify any

    def __str__(self):
        return self.username
