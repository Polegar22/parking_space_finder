from django.db import models

# Create your models here.
class ParkingSpot(models.Model):
    creationDate = models.DateField()
    lat = models.DecimalField()
    lon = models.DecimalField()
    type = models.TextField()
    size = models.TextField()
    plannedDuration = models.TextField()
    comment = models.TextField()

