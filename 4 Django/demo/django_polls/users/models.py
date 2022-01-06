from django.db import models
# AbstractUser class has all the same attributes and 
# functionality as the default User class but is made for extending
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    # additional User fields can be added here
    # but for now we'll just pass
    pass


    def __str__(self):
        return self.username

