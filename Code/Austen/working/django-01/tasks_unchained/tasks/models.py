from django.db.models import Model, CharField

# Create your models here.
class Task(Model):
  task_name = CharField(max_length=20)
  
  def __str__(self):
    return self.task_name