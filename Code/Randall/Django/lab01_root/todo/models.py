from django.db import models

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False) #did have a completed field. Deleted it but leaving in for now. 
    #item_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item + str(self.completed)