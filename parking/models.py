from django.db import models
from residents.models import Resident

class ParkingSlot(models.Model):
    SLOT_TYPE_CHOICES = (
        ('TWO_WHEELER', 'Two Wheeler'),
        ('FOUR_WHEELER', 'Four Wheeler'),
    )
    slot_number = models.CharField(max_length=10, unique=True)
    slot_type = models.CharField(max_length=20, choices=SLOT_TYPE_CHOICES)
    resident = models.OneToOneField(Resident, on_delete=models.SET_NULL, null=True, blank=True, related_name='parking_slot')

    def __str__(self):
        return f"Slot {self.slot_number} ({self.slot_type})"
