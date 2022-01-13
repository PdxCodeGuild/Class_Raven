from django.contrib import admin

# Register your models here.
from .models import (
    Priority,
    TodoItem
)

admin.site.register(Priority)
admin.site.register(TodoItem)