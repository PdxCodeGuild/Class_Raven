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
            "first_name": forms.TextInput(attrs={'class':'input'}),
            "last_name": forms.TextInput(attrs={'class':' input'}),
            "username": forms.TextInput(attrs={'class':'input', 'placeholder':'Username'}),
            "password": forms.PasswordInput(attrs={'class':'input', 'placeholder':'Password'}),
            "avatar": forms.FileInput(attrs={'class':'control file has-name is-right'}),
        }
        

class UserAuthorizeForm(UserForms):
    
    class Meta(UserForms.Meta):
        fields = ["username", "password"]