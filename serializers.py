from rest_framework import serializers

#load django and webapp models
from django.contrib.auth.models import *
from fuelup.api.models import *

class FillupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fillup
        fields = ('id', 'date', 'miles', 'gallons', 'pricePerGallon', 'vehicle')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'year', 'make', 'model', 'trim')

class FuelupuserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.filter(username=request.user.username))
    class Meta:
        model = Fuelupuser
        fields = ('id', 'user', 'vehicles')