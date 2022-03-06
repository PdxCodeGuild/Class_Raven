from django.db import models
from users.models import CustomUser


class Priority(models.Model):

    PRIORITY_CHOICES = [
        (0, "Completed"),
        (1, "Low"),
        (2, "Medium"),
        (3, "High"),
    ]
    name = models.IntegerField(choices=PRIORITY_CHOICES, default=2)

    def __str__(self):
        if self.name == 1:
            return "Low"
        elif self.name == 2:
            return "Medium"
        elif self.name == 3:
            return "High"
        elif self.name == 0:
            return "Completed"

    class Meta:
        verbose_name_plural = "Priorities"
        ordering = ["name"]


class TodoItem(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    priority = models.ForeignKey("Priority", on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-priority"]
