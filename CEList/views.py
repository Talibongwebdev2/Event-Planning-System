from django.shortcuts import render, redirect
from django.http import HttpResponse
from CEList.models import Customers_Profile, Booking, Event_Guest, Services, Adds_On, Budget


def home_page(request):
    cuslist = Customers_Profile.objects.all()
    return render(request, 'homepage.html', {'cuslist':cuslist})

def booking_view(request, cId):
    cusId = Customers_Profile.objects.get(id=cId)
    Booking.objects.create(customers_profile=cusId,event_type=request.POST['event_name'],venue=request.POST['venue_name'],date_time=request.POST['datentime'])
    return redirect(f'/CEList/{cusId.id}/')  


def events_page(request, cId):
    cusId = Customers_Profile.objects.get(id=cId)
    return render(request, 'eventsview.html', {'cusId': cusId})


def custom_view(request):
    cusProfile = Customers_Profile.objects.create( customers_name=request.POST['custom_name'],address=request.POST['custom_add'],book_date =request.POST['booking_date'],contact_number =request.POST['contact_num'])
    return redirect(f'/CEList/{cusProfile.id}/')

'''
def guest_view(request, list_id):
    eventId = Customers_Profile.objects.get(id=cId)
    return render(request, 'guest.html', {'customers_profile': cusId})

def third_model(request):
    eventId = booking.objects.get(id=cId)
    #Event_Guest.objects.create(booking=eventId,guest_names=request.POST['guest_name'], 'booking': eventId)
    return redirect(f'/CEList/{eventId.id}/')

def services_view(request, list_id):
    eventId = Customers_Profile.objects.get(id=cId)
    return render(request, 'guest.html', {'customers_profile': cusId})

def fourth_model(request):
    eventId = booking.objects.get(id=cId)
    #Event_Guest.objects.create(booking=eventId,guest_names=request.POST['guest_name'], 'booking': eventId)
    return redirect(f'/CEList/{eventId.id}/')
'''
'''
def defaultEntry(request):
	#Creating data
	customer = Customers_Profile(customers_name="Cesar Talibong", address="B. 28 L. 71 Viva Homes", book_date="05/15/2021" )
	customer = Customers_Profile(customers_name="Raymond Loon", address="B. 21 L. 15 Dexterville", book_date="05/13/2021" )
	customer.save()

	#Read all data
	customers = Customers_Profile.objects.all()
	result = 'Printing all customers list : <br>'
	for x in customers:
		res += X.customers_name+"<br>"

	#Read one data
	cusname = Customers_Profile.get(id="19")
	res += "Printing one customer profile : <br>"
	res += cusname.address

	#Delete data
	res+= '<br> Deletinng... <br>'
	cusname.delete()

	#Update/Creating data
	customer = Customers_Profile(customers_name="Ryan Balota", address="Avida Homes", book_date="05/15/2021")
	customer.save()
	res += 'Updating...<br>'

	#Update data
	customer = Customers_Profile.objects.get(customers_name="Raymond Loon")
	customer.venue = "Orchard golf and country club"
	customer.save()
	res = ""

	#Filtering data
	qs = Booking.objects.filter(customers_name="Raymond Loon")
	res += "found : %s result<br>"%len(qs)

	#ordering data
	qs = Customers_Profile.objects.order_by("book_date")
	for x in qs: 
		res += x.customers_name + x.address + '<br>'




'''