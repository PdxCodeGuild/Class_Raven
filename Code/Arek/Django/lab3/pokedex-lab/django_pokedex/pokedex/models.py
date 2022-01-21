from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import IntegerField

# Create your models here.

class User(AbstractUser): #in order to migrate this successfully, do not migrate before this is create like in the django quickstart
    pass # since abstract already has the fields that we need, we dont need to specify any

    def __str__(self):
        return self.username

#IMPORTANT: Make sure you add AUTH_USER_MODEL = 'myapp.User' to the bottom of the projects 'settings.py' file
# also make sure to add from 'django.contrib.auth.admin import UserAdmin' and 'admin.site.register(User, UserAdmin)'
# to your apps 'admin.py' file. 
#If you forget to do these 2 things your migration will fail.

class PokemonType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=20)
    height = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    image_front = models.CharField(max_length=100)
    image_back = models.CharField(max_length=100)
    types = models.ManyToManyField(PokemonType)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

