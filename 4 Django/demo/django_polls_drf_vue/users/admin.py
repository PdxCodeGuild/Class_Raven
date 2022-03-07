from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# register the CustomUser model and UserAdmin panel
# so they appear in admin/
admin.site.register(CustomUser, UserAdmin)
