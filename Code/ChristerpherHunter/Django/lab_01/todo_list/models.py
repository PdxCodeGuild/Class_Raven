from django.db import models

# Create your models here.


class TodoItem(models.Model):

    todo_name = models.CharField(max_length=30, default="none")

    text = models.TextField(max_length=150)

    created_date = models.DateTimeField(auto_now_add=True) 

    RADIO_CHOICES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]

    priority = models.CharField(
        max_length=6, choices=RADIO_CHOICES, default='medium')


