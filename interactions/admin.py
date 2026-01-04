from django.contrib import admin
from .models import Interaction

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ("id", "get_company", "client", "channel", "direction", "created_at", "next_action_at")
    list_filter = ("channel", "direction", "created_at", "client__company")
    search_fields = ("client_name", "clientemail", "clientphone", "clientcompany_name", "subject", "notes")
    autocomplete_fields = ("client",)
    ordering = ("-created_at",)

    @admin.display(description="Company")
    def get_company(self, obj):
        return obj.client.company.name