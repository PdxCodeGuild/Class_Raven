from django.contrib import admin

from .models import Priority, Todoitem

# Register your models here.
admin.site.register(Priority)
admin.site.register(Todoitem)