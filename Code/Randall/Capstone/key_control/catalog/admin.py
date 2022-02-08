from django.contrib import admin
from .models import Lock, KeyId, KeyInstance

#admin.site.register(KeyId)
admin.site.register(Lock)
#admin.site.register(KeyInstance)

class KeyInstanceInline(admin.TabularInline):
    model = KeyInstance
    extra = 0

# Register admin classes for KeyId using the decorator
@admin.register(KeyId)
class KeyAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_usefor')
    inlines = [KeyInstanceInline]

@admin.register(KeyInstance)
class KeyInstanceAdmin(admin.ModelAdmin):
    list_display = ('key', 'status', 'borrower', 'due_back', 'id')        ###Double check of key or keyid
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('key', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )