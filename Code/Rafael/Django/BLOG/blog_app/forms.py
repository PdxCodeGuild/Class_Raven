from django import forms
from .models import User
from django.forms import widgets



#create a model form to create your own fields for the users models
class UserForm(forms.ModelForm):
    """ 
    meta class describes the data included in the database model, that has fields from that model through the html fields
    """
    class Meta:
        model = User
# to include all fields
        #fields = '__all__'    
        
        fields = [
            'first_name', 
            'last_name', 
            'email'
            #'user_pic', 
            ]
    # You can customize with widgets to render in the html class/id using 'attrs='.
    '''
    widgets = [ 'first_name': forms.TextInput (attrs={'class':form-control'}),
                 'xxxxx': forms.xxxxx (attrs={'class':xxxxx'}),]
    '''

    # Bootstrap class assignments
"""
    widgets = {
        'first_name': forms.TextInput (attrs={'class':'form-control'}),
        'last_name': forms.TextInput (attrs={'class': 'form-control'}),
        'username': forms.TextInput (attrs={'class':'form-control'}),
        'password': forms.PasswordInput (attrs={'class':'form-control'}),
        'email':forms.TextInput (attrs={'class':'form-control'}),
        'user_pic': forms.FileInput (attrs={'class':'form-control'}),

    }

"""

# This class overrides the default fields and displays the fields in the dictionary.
class UserAuthForm(UserForm): 
    class Meta(UserForm.Meta):
        fields = [
            'username',
             'password',
             'first_name', 
             'last_name',
             'email',
             ]

