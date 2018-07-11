from rest_framework import serializers

from spacefinder.models import ParkingSpot


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'creationDate', 'lat', 'lon', 'type', 'size', 'plannedDuration', 'comment')
        model = ParkingSpot