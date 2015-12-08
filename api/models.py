from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from decimal import Decimal
from datetime import datetime
from fuelup.api.validators import *

# Create your models here.
class Vehicle(models.Model):
    """
    This is a vehicle entry for user submitted vehicle entries.
    """
    year = models.IntegerField(blank=False)
    make = models.CharField(max_length=15, blank=False, validators=[removeJavascriptKeyword])
    model = models.CharField(max_length=15, blank=False, validators=[removeJavascriptKeyword])
    trim = models.CharField(max_length=15, blank=False, validators=[removeJavascriptKeyword])
    def __str__(self):
         return str(self.id)+": "+str(self.year)+" "+str(self.make)+" "+str(self.model)+" "+str(self.trim)

    class Meta:
        verbose_name_plural = "Vehicles"

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('year', 'make', 'model', 'trim')

class Fillup(models.Model):
	"""
	This is a fillup entry for user submitted fillup entries
	"""
	date = models.DateField(blank=False)
	miles = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
	gallons = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
	pricepergallon = models.DecimalField(max_digits=4, decimal_places=3, blank=False)
	vehicle = models.ForeignKey(Vehicle, null=True)
    # def __str__(self):
    #     return str(self.id)+": "+str(self.date)+" "+str(self.miles)+" "+str(self.gallons)+" "+str(self.pricePerGallon)

	class Meta:
		verbose_name_plural = "Fillups"

class FillupAdmin(admin.ModelAdmin):
	list_display = ('date', 'miles', 'gallons', 'pricepergallon', 'vehicle')

class Fuelupuser(models.Model):
    """
    This is for storing user entries.
    """
    user = models.ForeignKey(User)
    vehicles = models.ManyToManyField(Vehicle, blank=True)
 		
    class Meta:
        #This will be used by the admin interface
        verbose_name_plural = "Users"

class FuelupuserAdmin(admin.ModelAdmin):
    #This inner class indicates to the admin interface how to display a User
    #See the Django documentation for more information
    list_display = ('user',)
