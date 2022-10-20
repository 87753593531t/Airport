from django.contrib import admin
from airport.models import Arrival_city, Departure_city, Flight

admin.site.register(Arrival_city)
admin.site.register(Departure_city)
admin.site.register(Flight)
