from django import forms
from .models import User


class UserForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            'first_name',
            'last_name',
        ]


        widgets = {
            'first_name': forms.TextInput(attrs={'id':'input_field'}),
            'last_name': forms.TextInput(attrs={'id':'input_field'}),
            'username': forms.TextInput(attrs={'id':'input_field','class': 'input_class', 'placeholder':'Enter username'}),
            'password': forms.PasswordInput(attrs={'id':'input_field','class': 'input_class', 'placeholder':'Enter password'})
        }


class UserAuthForm(UserForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'password']