from django.db import models
from django.db.models.fields import BooleanField, DateTimeField
from django.db.models.fields.related import ForeignKey
from users.models import CustomUser
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=3000)
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogpost')
    public = models.BooleanField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_edited=models.DateTimeField(auto_now=True)

def __str__(self):
        return f"{self.title} {self.body} {self.user} {self.created_date}"