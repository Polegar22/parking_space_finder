from rest_framework import generics

from spacefinder import ParkingSpotSerializer
from spacefinder.models import ParkingSpot


class ParkingSpotList(generics.ListCreateAPIView):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

