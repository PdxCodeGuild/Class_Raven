from django import forms
from .models import User

class UserForm(forms.ModelForm):
    # the Meta class wil describe the data used to create the form
    # this includes the DB Model, which fields from that model
    # and the widgets (HTML templates that) should be used for each field
    class Meta:
        # this form is for creating/editing objects from the User model
        model = User

        # fields = '__all__' # include all fields
        fields = [
            'first_name',
            'last_name',
            'avatar'
        ]

        # customize the HTML that will be rendered when the form is rendered
        # 'form-control' is a 
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'id':'abcdefg'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'avatar': forms.FileInput(attrs={'class':'form-control'}),
        }

class UserAuthForm(UserForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'password']
