from django.db import models

# Create your models here.

user_choices = [
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low')
]

class Priority(models.Model):
    name = models.CharField(max_length=6, default='medium', choices=user_choices)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    text = models.CharField('Todo Item', max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='choices')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text}, {self.created_date}, {self.priority.name}'
