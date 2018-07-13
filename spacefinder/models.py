from django.db import models

# Create your models here.
class ParkingSpot(models.Model):
    creationDate = models.DateTimeField(auto_now=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    type = models.TextField(blank=True)
    size = models.TextField(blank=True)
    plannedDuration = models.TextField(blank=True)
    comment = models.TextField(blank=True)

