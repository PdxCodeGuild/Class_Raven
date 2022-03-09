from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.



public = (
    ('yes', 'yes'),
    ('no', 'no'),
    
)



class Post(models.Model):
    title = models.CharField(max_length=40, null=True, blank=True, default='')
    body = models.CharField(max_length=1000)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='post')
    public = models.CharField(max_length=30, choices=public, default='Full Time', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
 
    


    def __str__(self):
        return self.user.username 


