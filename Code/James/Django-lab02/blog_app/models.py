from django.db import models
from django.contrib.auth import get_user_model

from users_app.models import User

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(User(), on_delete=models.CASCADE, related_name='user')
    public = models.BooleanField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'