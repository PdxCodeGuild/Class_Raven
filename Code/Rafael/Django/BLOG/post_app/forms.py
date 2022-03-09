from django import forms

from .models import Post

from django.forms import widgets

class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post 
        fields = [
            'title',
            'body',
            'user',
            'public',
            #'created_at',
            #'updated_at'
   
         ]
# widgets are not working at this time 3/3/2022

