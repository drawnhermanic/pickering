from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"

class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    details = models.CharField(max_length=5000)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    visitors = models.IntegerField()
    request_date = models.DateTimeField()
    approval_uuid = models.UUIDField()
    approved = models.BooleanField()
    approval_date = models.DateTimeField()
    