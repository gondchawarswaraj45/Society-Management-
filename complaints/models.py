from django.db import models
from django.conf import settings

class Complaint(models.Model):
    CATEGORY_CHOICES = (
        ('WATER', 'Water'),
        ('ELECTRICITY', 'Electricity'),
        ('SECURITY', 'Security'),
        ('PLUMBING', 'Plumbing'),
        ('OTHERS', 'Others'),
    )
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='complaints')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.subject} - {self.status}"
