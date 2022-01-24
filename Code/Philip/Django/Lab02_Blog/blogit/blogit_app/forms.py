from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'public')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'give your thoughts a title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'tell us what its about'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'go ahead, get creative'}),
            'public': forms.NullBooleanSelect(attrs={'class': 'form-control', 'placeholder':'would you like the world to know?'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'public')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'give your thoughts a title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'tell us what its about'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'go ahead, get creative'}),
            'public': forms.NullBooleanSelect(attrs={'class': 'form-control', 'placeholder':'would you like the world to know?'}),
        }