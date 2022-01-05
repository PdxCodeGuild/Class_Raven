from django.db import models

class Priority(models.Model): 
    priority = models.CharField(max_length=7)
   
    def __str__(self):
        return self.priority

class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    priority_choice = models.ForeignKey(Priority, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title