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
            'first_name': forms.TextInput(attrs={'id':'form_field'}),
            'last_name': forms.TextInput(attrs={'id':'form_field'}),
            'username': forms.TextInput(attrs={'id':'form_field'}),
            'password': forms.PasswordInput(attrs={'id':'form_field'})
        }


class UserAuthForm(UserForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'password']