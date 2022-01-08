from typing import Text
from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.db.models.fields import CharField
from django.db import models

# Create your models here.

STATUS_CHOICES = [
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low')
]


class Priority(models.Model):
    name = models.CharField(max_length=6, choices=STATUS_CHOICES, default='low')

    def __str__(self):
        return self.name


class Todoitem(models.Model):
    text = models.CharField('Todo item', max_length=200)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, related_name='choices')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        print(type(self.priority.name))
        return f'{self.text}, {self.created_date}, {self.priority.name}'
