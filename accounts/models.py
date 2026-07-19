from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('SECRETARY', 'Secretary'),
        ('TREASURER', 'Treasurer'),
        ('RESIDENT', 'Resident'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='RESIDENT')
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
