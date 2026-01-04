from django.db import models
from companies.models import Company


class Client(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="clients")
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.company.name})"