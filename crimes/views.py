from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

from foiaqui.crimes.models import Incident

from datetime import datetime

def index(request):
	""" Sends a XML file with some incidents """
	incident_list = Incident.objects.all()
	response = render_to_response('crimes/list.xml', {'incident_list': incident_list})
	response['Content-Type'] = 'text/xml'
	response['Content-Disposition'] = "attachment; filename=list.xml"
	return response

def insert_incident(request):
	""" Calls that when you want to insert an incident by POST """
	
	# Get current time and date from the server
	now = datetime.now()
	
	# From POST we get desc, lat, lng
	desc = request.POST.get('desc', '')
	lat = request.POST.get('lat', '')
	lng = request.POST.get('lng', '')
	
	# Create a new incident and save it
	new_incident = Incident(desc=desc, lat=lat, lon=lng, when=now)
	new_incident.save()
	
	# If we got all parameters
	if desc and lat and lng:
		return HttpResponse('desc=%s<br/>lat=%s<br/>lng=%s<br/>'%(desc,lat,lng))
	
	# If one or more are missing
	else:
		return HttpResponse('One or more parameters are missing ...<br/>desc=%s<br/>lat=%s<br/>lng=%s<br/>'%(desc,lat,lng))
		

