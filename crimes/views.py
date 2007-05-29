from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404
from foiaqui.crimes.models import Incident

def index(request):
    incident_list = Incident.objects.all()
    response = render_to_response('crimes/list.xml', {'incident_list': incident_list})
    response['Content-Type'] = 'text/xml'
    response['Content-Disposition'] = "attachment; filename=list.xml"
    return response
