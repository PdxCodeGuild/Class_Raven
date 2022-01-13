from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.db.models.fields import CharField
from django.db import models

CHOICES=[
    ('low','Low'),
    ('medium','Medium'),
    ('high','High'),
]

class Priority(models.Model):
    priority= models.CharField(choices=CHOICES,max_length=20)

    def __str__(self):
        return self.priority

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    priority_choice = models.ForeignKey(Priority,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title + self.priority_choice