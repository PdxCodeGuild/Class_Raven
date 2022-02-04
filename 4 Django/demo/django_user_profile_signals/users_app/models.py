from django.db import models
from django.contrib.auth.models import AbstractUser

# can't import Profile here because of circular import
# from profiles_app.models import Profile
class User(AbstractUser):

    def __str__(self):
        return self.username


    # def save(self, *args, **kwargs):
    #     # do something before saving the user
    #     # new_user = super(User, self).save(*args, **kwargs)
    #     # Profile.objects.create(user=new_user)
    #     pass