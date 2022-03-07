from django import forms
from django.contrib.auth import get_user_model
from profiles_app.models import Profile

class RegisterForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


    def save(self, commit=True):
        # create a User instance from a copy of the RegisterForm
        user_instance = super(RegisterForm, self).save(commit=False)
        user_instance.set_password(self.cleaned_data['password'])
        user_instance.save()

        # create a Profile object for the user
        # Profile.objects.create(user=user_instance)

        return user_instance