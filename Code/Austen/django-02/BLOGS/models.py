from django.db.models import *
from django.contrib.auth import get_user_model

# Create your models here.
class Blog(Model):
    user = OneToOneField(get_user_model(), on_delete=CASCADE)

class Post(Model):
    blog = ForeignKey(Blog, on_delete=CASCADE)
    title = CharField(max_length=24)
    content = CharField(max_length=100)