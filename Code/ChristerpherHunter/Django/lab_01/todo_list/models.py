from django.db import models

# Create your models here.


class Priority(models.Model):

    RADIO_CHOICES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]

    priority_value = models.CharField(
        max_length=6, choices=RADIO_CHOICES, default='medium')

    def __str__(self) -> str:
        return self.priority_value


class TodoItem(models.Model):

    todo_name = models.CharField(max_length=30, default="none")

    text = models.TextField(max_length=150)

    created_date = models.DateTimeField(auto_now_add=True)

    completed_or_not = models.BooleanField(default=False)

    priority = models.ForeignKey(
        to=Priority, on_delete=models.SET_NULL, related_name="todos", null=True)
