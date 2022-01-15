from dataclasses import fields
from distutils.command.clean import clean
from django import forms
from .models import UserInfo


class UserForms(forms.ModelForm):

    

    class Meta:

        model = UserInfo

        fields = [
            "first_name",
            "last_name",
            "avatar"
        ]

        # Customize the rendered HTML
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'input'}),
            "last_name": forms.TextInput(attrs={'class': ' input'}),
            "username": forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}),
            "password": forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}),
            "avatar": forms.FileInput(attrs={'class': 'control file has-name is-right'}),
        }


class UserAuthorizeForm(UserForms):

    class Meta(UserForms.Meta):

        fields = [
            "username",
            "password",
        ]


class UserCreationsForm(UserForms):

    re_password = forms.CharField(max_length=40,
                                            widget=forms.PasswordInput(attrs={
                                                'autocomplete': 'new-password',
                                                'class': 'input',
                                                'placeholder': 'Password'
                                            }))

    def clean(self):
        cleaned_data = super(UserCreationsForm, self).clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password != re_password:
            self.add_error("re_password", "Passwords do not match!")

        return cleaned_data
    
    class Meta(UserForms.Meta):

        
        fields = [
            "username",
            "password",
            "re_password"
        ]
