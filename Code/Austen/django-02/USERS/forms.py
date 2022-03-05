from django.forms import *
from django.contrib.auth import get_user_model
from BLOGS.models import Blog
class user:
    class login(ModelForm):
        class Meta:
            model = get_user_model()
            fields = ['username', 'password']
            widgets = {'password': PasswordInput()}
    
    class register(ModelForm):
        class Meta:
            model = get_user_model()
            fields = ['username', 'email', 'password']
        def save(self, commit=True):
            new_user = super(user.register, self).save(commit=False)
            new_user.username = self.cleaned_data['username']
            new_user.set_password(self.cleaned_data['password'])
            if commit:
                new_user.save()
                user_blog = Blog.objects.create(user=new_user)
            return new_user
    
    class update:
        class email(ModelForm):
            class Meta:
                model = get_user_model()
                fields = ['email']
        
        class password(ModelForm):
            class Meta:
                model = get_user_model()
                fields = ['password']
