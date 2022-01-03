from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    """
    Custom user model
    """

    pass


def __str__(self):
    return self.username
