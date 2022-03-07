from django.contrib import admin

# Register your models here.
from .models import Todoitem, Priority


admin.site.register(Priority)
admin.site.register(Todoitem)