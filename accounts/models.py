from django.db import models
from django.contrib.auth.models import User
from companies.models import Company

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="profiles")

    def _str_(self):
        return f"{self.user.username} -> {self.company.name}"