from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


# Create your models here.
TODO_PRIORITY_LIST = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    )
class Priority(models.Model):
    priority = models.CharField(max_length=1, choices=TODO_PRIORITY_LIST)

    def __str__(self):
        return self.priority

class TodoItem(models.Model):
    todo_text = models.CharField(max_length=200)
    todo_priority = ForeignKey(Priority, on_delete=CASCADE, related_name='todo_priority')
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.todo_text