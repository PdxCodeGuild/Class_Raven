from django.contrib import admin

# import the model class from the polls/models.py
from .models import Question

# register the model so it will appear in the admin panel
admin.site.register(Question)
