from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField  

# Create your models here.

class User(AbstractUser): #in order to migrate this successfully, do not migrate before this is create like in the django quickstart
    pass # since abstract already has the fields that we need, we dont need to specify any

    def __str__(self):
        return self.username
        
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
