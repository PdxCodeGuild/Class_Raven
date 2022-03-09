from django.db import models
from django.utils import timezone
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

choices = [('h', 'High'), ('m', 'Medium'), ('l', 'Low'),]
        

class Priority(models.Model):
   
    priority = models.CharField(
        max_length=10, 
        choices=choices, default="m"
        )

    def __str__(self):
        return self.priority



class MyModel(models.Model):
    mymodel = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False, null=True)
    priority = models.CharField(max_length=30, null=True, choices=choices, default="")
   

    def __str__(self):
        return self.mymodel

