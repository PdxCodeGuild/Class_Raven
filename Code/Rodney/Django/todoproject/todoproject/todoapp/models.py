from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


PRIORITY_CHOICES = (
    ("HIGH", "High"),
    ("MEDIUM", "Medium"),
    ("LOW", "Low"),
)

class Priority(models.Model):
    priority_level = models.CharField(max_length=20, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.priority_level

class TodoItem(models.Model):
    item_text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.item_text

