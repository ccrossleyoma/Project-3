from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from decimal import Decimal
from datetime import datetime

# Create your models here.
class Fillup(models.Model):
	"""
	This is a fillup entry for user submitted fillup entries
	"""
	date = models.DateField(auto_now_add=True, blank=False)
	miles = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
	gallons = models.DecimalField(max_digits=3, decimal_places=2, blank=False)
	pricePerGallon = models.DecimalField(max_digits=3, decimal_places=3, blank=False)

	class Meta:
		verbose_name_plural = "Fillups"

class FillupAdmin(admin.ModelAdmin):
	list_display = ('user', 'date', 'miles', 'gallons', 'pricePerGallon', 'vehicle')

class Vehicle(models.Model):
    """
    This is a vehicle entry for user submitted vehicle entries.
    """
    year = models.DecimalField(max_digits=4, decimal_places=0, blank=False)
    make = models.CharField(max_length=40, blank=False)
    model = models.CharField(max_length=40, blank=False)
    trim = models.CharField(max_length=40, blank=False)
    fillups = models.ForeignKey(Fillup, unique=False)
 	# def __str__(self):
 	# 	return str(self.id)+":"+self.name

    class Meta:
        verbose_name_plural = "Vehicles"

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('year', 'make', 'model', 'trim', 'user', 'fillups')

class User(models.Model):
    """
    This is for storing user entries.
    """
    username = models.CharField(max_length=40, blank=False)
    password = models.CharField(max_length=40, blank=False)
    vehicles = models.ForeignKey(Vehicle, unique=False)
    fillups = models.ForeignKey(Fillup, unique=False)
   #  def __str__(self):
 		# return str(self.id) +self.username
 		
    class Meta:
        #This will be used by the admin interface
        verbose_name_plural = "Users"

class UserAdmin(admin.ModelAdmin):
    #This inner class indicates to the admin interface how to display a post
    #See the Django documentation for more information
    list_display = ('username', 'password', 'vehicles', 'fillups')
