from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.db.models.fields import CharField
from django.db import models



class Priority(models.Model):
    priority= models.CharField(max_length=20)

    def __str__(self):
        return self.priority

priority, created = Priority.objects.get_or_create(priority='High')
priority, created = Priority.objects.get_or_create(priority='Medium')
priority, created = Priority.objects.get_or_create(priority='Low')

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    priority_choice = models.ForeignKey(Priority,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title + self.priority_choice