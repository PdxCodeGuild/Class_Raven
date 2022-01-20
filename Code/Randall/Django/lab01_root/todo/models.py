from django.db import models
from datetime import datetime
from django.http import HttpResponse
from django.utils import timezone



class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False) 
    #created_date=models.DateTimeField(default=True)

    def __str__(self):
        return self.item + str(self.completed) #   + str(self.created_date)

"""
def index(request):
    time_created = [timezone.now()]
    return HttpResponse(time_created)
"""