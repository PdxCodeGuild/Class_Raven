from django import forms
from django.forms import models
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ["mymodel", "completed",]
        #fields = ["mymodel", "completed", "priority"]