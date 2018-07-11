from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^parkings/$', views.ParkingSpotList.as_view()),
]
