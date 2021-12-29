from django.contrib import admin

# import the model class from the polls/models.py
from .models import Question, Choice

# register the model so it will appear in the admin panel
admin.site.register(Question)
admin.site.register(Choice)
