# Django
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Python
from datetime import datetime

# foiaqui
from foiaqui.crimes.models import Incident

def xml(request):
	""" Sends a XML file with some incidents """
	incident_list = Incident.objects.all()
	response = render_to_response('crimes/list.xml', {'incident_list': incident_list})
	response['Content-Type'] = 'text/xml'
	response['Content-Disposition'] = "attachment; filename=list.xml"
	return response


def insert(request):
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


def form(request):
	""" Displays a form of a new incident """
	
	if request.method == 'POST':
		mobility = request.POST.get("mobility", "")
		quantity = request.POST.get("quantity", "")
		thief = request.POST.get("thief", "")
		weapon = request.POST.get("weapon", "")
		period = request.POST.get("period", "")
		desc = request.POST.get("desc", "")

		lat = request.POST.get("lat", "0")
		lng = request.POST.get("lng", "0")
		print 'eis: ',lat, lng

		# If this request come from the main site (the map), the form should know only desc.
		from_main = request.POST.get("from_main", "False")
		if from_main == "True":
			return render_to_response('crimes/form.html', {'desc':desc, 'lat':lat,'lng':lng})

		# If we have all stuff we need, lets create a incident and save it.
		if mobility and quantity and thief and weapon and period and desc:
			# we get the local time
			now = datetime.now()
			# creates a new incident and save it
			new_incident = Incident(desc=desc, when=now, mobility=mobility, quantity=quantity, thief=thief, weapon = weapon, period=period, lat=lat, lon=lng)
			new_incident.save()
			return 
			#return HttpResponse('urru')
		
		# If everything else fails, we call form.html but passing what we have.
		return render_to_response('crimes/form.html',{'mobility': mobility,'quantity':quantity, 'thief': thief, 'weapon':weapon, 'period':period, 'desc':desc, 'lat':lat, 'lng':lng, 'from_main':from_main})
	else:
		return HttpResponseRedirect('/')
#		return HttpResponse('Acesse o site principal para criar um novo incidente')
#		return render_to_response('base.html')


def detail(request, id='1'):
	""" Displays a detailed view of an incident"""
	i = get_object_or_404(Incident, pk=id)
	return render_to_response('crimes/detail.html',{'incident':i})
	#i = Incident.objects.all().get(pk=id)
	#return render_to_response('crimes/form.html',{'incident':i})

