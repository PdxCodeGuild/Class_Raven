from django.db.models import *
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your models here.


class Post(Model):
    blog = ForeignKey('Blog', on_delete=CASCADE)
    title = CharField(max_length=24)
    content = CharField(max_length=100)
    created = DateTimeField(auto_now_add=True)
    edited = DateTimeField(default=datetime.now())
    public = BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

class Blog(Model):
    user = OneToOneField(get_user_model(), on_delete=CASCADE)
    posts = ManyToManyField(Post, related_name='blogs', blank=True)

    def __str__(self):
        return f'{self.user}\'s blog'