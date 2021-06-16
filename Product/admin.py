from django.contrib import admin

# Register your models here.

from .models import Product

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'weight', 'price', 'created_at', 'updated_at']