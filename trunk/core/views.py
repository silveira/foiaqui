from django.shortcuts import render_to_response
from foiaqui.crimes.models import Incident


def index(request):
	# How many incidents we have
	n = Incident.objects.count()

	# Transform in a language text
	if n == 0:
		text = "Nao ha nenhum incidente registrado."
	elif n == 1:
		text = "Atualmente nos temos <strong>%d</strong> incidente registrado." % n
	else:
		text = "Atualmente nos temos <strong>%d</strong> incidentes registrados." % n

	# get all incidents
	list = Incident.objects.all()

	return render_to_response('base.html', {'incident_list':list, 'incident_counter_text':text})
