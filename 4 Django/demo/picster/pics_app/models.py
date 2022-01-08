from django.db import models
from django.contrib.auth import get_user_model

from users_app.models import User
# instance - the User object to which the ImageField is being attached
def get_upload_path(instance, filename):
    return f'images/pics/{filename}'

class Pic(models.Model):
    image = models.ImageField(upload_to=get_upload_path)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='pics')
    caption = models.CharField(max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True)
    
    likes = models.ManyToManyField(get_user_model(), related_name='users', blank=True)

    def __str__(self):
        return self.user.username + ' - ' + self.image.url