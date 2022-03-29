from django.contrib import admin

from .models import Cart, Category, Product

admin.site.register([Cart, Category, Product])