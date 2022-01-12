from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey
from users_handler import models

# Create your models here.

class BlogPost(models.Model):

    title = CharField(max_length=40)

    body = TextField(max_length=200)

    user = ForeignKey(to=models.UserTable)

    public = BooleanField(default=False)

    date_created = DateTimeField(auto_now_add=True)

    date_edited = DateTimeField(auto_now=True)