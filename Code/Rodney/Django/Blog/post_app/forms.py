from django import forms
from django.db.models import fields
from .models import BlogPost, User 



class BlogPostForm(forms.ModelForm):
    
    class Meta:

        model = BlogPost

        fields = [
            'blog_title',
            'blog_body',
            'public_post'
        ]

        widgets = {
            'blog_title': forms.TextInput(attrs={'class':'form-control'}),
            'blog_body': forms.Textarea(attrs={'class':'form-control'}),
           
        }

