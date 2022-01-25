from django import forms
from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]

        #Customize the HTML Class for each
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'id':'check-users-forms-py'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }

class UserAuthForm(UserForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'password', ]