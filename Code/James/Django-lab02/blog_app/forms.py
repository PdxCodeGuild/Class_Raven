from django import forms
from django.forms import fields, widgets


from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'style': 'resize: none', 'placeholder': 'Enter blog here'})
        }