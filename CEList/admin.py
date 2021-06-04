from django.contrib import admin
from .models import Customers_Profile, Booking, Event_Guest, Services, Adds_On, Budget


admin.site.register(Customers_Profile)
admin.site.register(Booking)
admin.site.register(Event_Guest)
admin.site.register(Services)
admin.site.register(Adds_On)
admin.site.register(Budget)