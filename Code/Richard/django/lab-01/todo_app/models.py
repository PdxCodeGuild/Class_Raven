from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Priority(models.Model):
    name = CharField(max_length=20)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    todo_item_text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=CASCADE, related_name='todoitems')

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.todo_item_text}/n {self.priority}  {self.created_date}"
