from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.fields import BLANK_CHOICE_DASH
from .models import User, BlogPost
# Register your models here.

admin.site.register(User, UserAdmin)

class BlogPostAdmin(admin.ModelAdmin): 
    # since these two fields below have the attributes (auto_now_add, and auto_now) set to True,
    # They do not show up in the admin panel, to get around that you add the below line of code
    
    readonly_fields = ('date_created', 'date_edited') #this will make the fields show up but not be editable

admin.site.register(BlogPost, BlogPostAdmin)
