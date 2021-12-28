from typing import Text
from django.db import models
from django.db.models.fields import CharField

# Create your models here.

STATUS_CHOICES = [
    ('high', 'High')
    ('medium', 'Medium')
    ('low', 'Low')
]

class Priority(models.Model):
    name = CharField('high', 'medium', 'low')



class Todoitem(models.Model):
    text = models.CharField(max_length=200),
    priority = models.ForeignKey(Priority),
    created_date = models.DateTimeField()
