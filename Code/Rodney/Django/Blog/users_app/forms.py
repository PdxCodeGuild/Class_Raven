from django import forms
from django.db.models import fields
from .models import User 

class UserForm(forms.ModelForm):

    #meta describes data used to make form, which fields, widgets, database model

    class Meta: 

        #this form is for the User model 
        model = User

        fields = [
            'first_name',
            'last_name',
            'user_blog_name',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'user_blog_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }


class UserAuthForm(UserForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'password']


