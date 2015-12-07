from django.contrib import admin
from fuelup.api.models import *
from django.contrib.sessions.models import Session

admin.site.register(Fillup, FillupAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Session)


