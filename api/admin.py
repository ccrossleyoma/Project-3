from django.contrib import admin
from fuelup.api.models import *

admin.site.register(Fillup, FillupAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(User, UserAdmin)