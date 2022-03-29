from django.apps import AppConfig
from django.contrib.auth import get_user_model

# post_save signal runs after a model instance is saved
from django.db.models.signals import post_save

from .signals import create_profile
class ProfilesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles_app'

    # ready() runs when the app is loaded

    # without the @receiver decorator on create_profile
    # def ready(self):
    #     # connect the create profile function to the post_save signal
    #     post_save.connect(create_profile, sender=get_user_model())

    # with the @receiver decorator on create_profile
    def ready(self):
        from . import signals