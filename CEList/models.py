from django.db import models


class Customers_Profile(models.Model):
    customers_name = models.TextField(default='')
    address = models.TextField(default='')
    book_date = models.DateTimeField(default='')
    contact_number = models.TextField(default='')

class Booking(models.Model):
    customers_profile = models.ForeignKey(Customers_Profile, default=None, on_delete=models.CASCADE)
    event_type = models.TextField(default='')
    venue = models.TextField(default='')
    date_time = models.DateTimeField(default='')
    
class Event_Guest(models.Model): 
    booking = models.ForeignKey(Booking, default=None, on_delete=models.CASCADE)
    guest_names = models.TextField(default='')

class Services(models.Model):
	booking = models.ForeignKey(Booking, default=None, on_delete=models.CASCADE)
	services = models.TextField(default='')

class Adds_On(models.Model):
	booking = models.ForeignKey(Booking, default=None, on_delete=models.CASCADE)
	additionals = models.TextField(default='')

class Budget(models.Model):
	booking = models.OneToOneField(Booking, default=None, on_delete=models.CASCADE)
	budget = models.TextField(default='')
	