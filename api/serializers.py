from rest_framework import serializers

#load django and webapp models
from django.contrib.auth.models import *
from fuelup.api.models import *

class FillupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fillup
        fields = ('id', 'date', 'miles', 'gallons', 'pricepergallon', 'vehicle')

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'year', 'make', 'model', 'trim')

class FuelupuserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Fuelupuser
        fields = ('id', 'user', 'vehicles')

# class SessionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Session
#         fields = ('username', 'userid', 'isauthenticated')