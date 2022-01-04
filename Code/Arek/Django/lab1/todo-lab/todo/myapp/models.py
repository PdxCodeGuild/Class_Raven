
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BLANK_CHOICE_DASH, CharField

# Create your models here.
# TodItem Model
priority_choices = [
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low')
]


class Priority(models.Model):
    name = models.CharField(max_length=6, choices=priority_choices)

    def __str__(self):
        return self.name

    

class Todoitem(models.Model):
    text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    created_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text # when I added the self.created_date, it gave me an error when adding a new todo item