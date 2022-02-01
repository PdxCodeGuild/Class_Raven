from asyncio.format_helpers import extract_stack
from django.contrib import admin
from .models import Lock, KeyId, KeyInstance

#admin.site.register(KeyId)
admin.site.register(Lock)
#admin.site.register(KeyInstance)

class KeyInstanceInline(admin.TabularInline):
    model = KeyInstance
    extra = 0

# Register the Admin classes for KeyId using the decorator
@admin.register(KeyId)
class KeyAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_usefor')
    inlines = [KeyInstanceInline]

# Register the Admin classes for KeyInstance using the decorator
@admin.register(KeyInstance)
class KeyInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')



