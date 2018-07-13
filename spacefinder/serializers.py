from rest_framework import serializers

from spacefinder.models import ParkingSpot


class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'creationDate', 'latitude', 'longitude', 'type', 'size', 'plannedDuration', 'comment')
        model = ParkingSpot