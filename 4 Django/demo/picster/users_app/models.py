from django.db import models
from django.contrib.auth.models import AbstractUser

# instance - the User object to which the ImageField is being attached
def get_upload_path(instance, filename):
    return f'images/avatars/{filename}'


class User(AbstractUser):

    avatar = models.ImageField(upload_to=get_upload_path, default='images/avatars/default_avatar.jpg')

    def __str__(self):
        return self.username