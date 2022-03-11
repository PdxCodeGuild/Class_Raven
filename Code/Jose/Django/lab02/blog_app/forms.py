from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost


        fields = [
        'title',
        'body'
        ]


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter text'})
        }
# Create blog attached attributes