from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Add user models to admin
from .models import User

# Register your models here.
# UserAdmin allows extra options in the admin panel
admin.site.register(User, UserAdmin)

