from rest_framework import serializers

#load django and webapp models
from django.contrib.auth.models import *
from myapp.api.models import *

class FillupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fillup
        fields = ('id', 'user', 'date', 'miles', 'gallons', 'pricePerGallon', 'vehicle')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'year', 'make', 'models', 'trim', 'user', 'fillups')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'vehicles', 'fillups')