from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser


def upload_path(instance, filename):
    return f"blog/static/img/avatars/{filename}"

# Create your models here.
class UserInfo(AbstractUser):

    avatar = models.ImageField(upload_to=upload_path, default="blog/static/img/avatars/default_avt.png")

    def __str__(self) -> str:
        return self.username