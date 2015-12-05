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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'vehicles')

# class SessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Session
#         fields = ('username', 'userid', 'isauthenticated')