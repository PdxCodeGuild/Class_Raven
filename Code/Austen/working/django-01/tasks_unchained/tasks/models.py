from django.db.models import Model, CharField, BooleanField

# Create your models here.
class Task(Model):
  name = CharField(max_length=20)
  status = BooleanField(default=False)
  
  def __str__(self):
    return self.name