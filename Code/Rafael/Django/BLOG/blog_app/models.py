from django.db import models
from django.contrib.auth import get_user_model
#from blog_app.models import User
# Import AbstractUser
from django.http import HttpResponse
from django.contrib.auth.models import AbstractUser



# Create your models here.
def get_upload_path(instance, filename, self, obj):
    if obj.user_pic:
        return f'static/images/user_images{filename}'
    else:
        return HttpResponse('no image availables')


# With AbstractUser you get all the fields as a user model, however now you can add additional fields, reccomended to do this before making migrations. 
class User(AbstractUser):
# Image folder where user_pic images are collated from .username
    user_pic = models.ImageField(upload_to='static/images/user_images/{filename}')

    def _str_(self):
        return self.username