from django.db import models
from clients.models import Client

class Interaction(models.Model):
    class Channel(models.TextChoices):
        WHATSAPP = "whatsapp", "WhatsApp"
        EMAIL = "email", "Email"
        CALL = "call", "Call"
        MEET = "meet", "Meet"
        INSTAGRAM = "instagram", "Instagram"
        WEB = "web", "Web"
        OTHER = "other", "Other"

    class Direction(models.TextChoices):
        OUT = "out", "Outgoing"
        IN = "in", "Incoming"

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="interactions")
    channel = models.CharField(max_length=20, choices=Channel.choices, default=Channel.WHATSAPP)
    direction = models.CharField(max_length=10, choices=Direction.choices, default=Direction.OUT)

    subject = models.CharField(max_length=120, blank=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    next_action_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def _str_(self):
        base = self.subject or f"{self.get_channel_display()} ({self.get_direction_display()})"
        return f"{self.client.name} - {base}"