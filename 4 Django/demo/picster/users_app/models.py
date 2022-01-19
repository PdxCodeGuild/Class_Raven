from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# instance - the User object to which the ImageField is being attached
def get_upload_path(instance, filename):
    return f'images/avatars/{filename}'


class User(AbstractUser):

    avatar = models.ImageField(upload_to=get_upload_path, default='images/avatars/default_avatar.jpg')

    # Normally many-to-many relationships are two-way connections
    # 'symmetrical = False' will only form the relationship one way
    # so the user that is followed has the choice to follow back instead of being automatically followed
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='following')

    def __str__(self):
        return self.username