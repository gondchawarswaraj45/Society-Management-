from django.db import models
from django.conf import settings

class Flat(models.Model):
    FLAT_TYPE_CHOICES = (
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
    )
    unit_number = models.CharField(max_length=10, unique=True)
    floor = models.IntegerField()
    flat_type = models.CharField(max_length=10, choices=FLAT_TYPE_CHOICES)
    
    def __str__(self):
        return f"Flat {self.unit_number}"

class Resident(models.Model):
    STATUS_CHOICES = (
        ('OWNER', 'Owner'),
        ('TENANT', 'Tenant'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='resident_profile')
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='residents')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OWNER')
    move_in_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.flat.unit_number})"

class FamilyMember(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='family_members')
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.relationship} of {self.resident.user.username}"
