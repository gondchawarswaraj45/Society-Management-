from django.db import models
from django.conf import settings
from residents.models import Resident

class MaintenanceBill(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='bills')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bill for {self.resident.user.username} - {self.month.strftime('%B %Y')}"

class Payment(models.Model):
    bill = models.OneToOneField(MaintenanceBill, on_delete=models.CASCADE, related_name='payment')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment for {self.bill}"
