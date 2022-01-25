from django.contrib import admin

from .models import Todo
from .models import Priority

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display=['title','created_date','priority_choice','completed']

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display=['priority']