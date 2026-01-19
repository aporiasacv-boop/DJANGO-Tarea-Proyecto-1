from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active", "created_at")
    search_fields = ("name",)
    list_filter = ("is_active",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "sku", "category", "price", "stock", "is_active", "created_at")
    search_fields = ("name", "sku", "category__name")
    list_filter = ("is_active", "category")
    autocomplete_fields = ("category",)