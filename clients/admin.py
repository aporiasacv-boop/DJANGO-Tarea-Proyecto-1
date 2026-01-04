from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    autocomplete_fields = ("company",)
    list_display = ("id", "name", "company", "email", "phone", "is_active", "created_at")
    search_fields = ("name", "email", "phone", "company__name")
    list_filter = ("is_active", "company", "created_at")
    list_display = ('name', 'email', 'company', 'is_active')
    list_filter = ('company', ('is_active'))