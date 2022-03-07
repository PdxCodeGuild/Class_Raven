
from django.dispatch import receiver
from django.db.models.signals import post_save
from main_proj.settings import AUTH_USER_MODEL
# sender - Model calling the signal
# instance - instance of the sender Model created after save
# **kwargs - additional keyword arguments
@receiver(post_save, sender=AUTH_USER_MODEL)
def create_profile(sender, instance, **kwargs):
    from .models import Profile

    # print('sender:', sender)
    # print('instance:', instance)
    # print('kwargs:', kwargs)

    Profile.objects.create(user=instance)