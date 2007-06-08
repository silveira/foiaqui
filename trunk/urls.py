from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^polls/$', 'foiaqui.polls.views.index'),
    (r'^polls/(?P<poll_id>\d+)/$', 'foiaqui.polls.views.detail'),
    (r'^polls/(?P<poll_id>\d+)/results/$', 'foiaqui.polls.views.results'),
    (r'^polls/(?P<poll_id>\d+)/vote/$', 'foiaqui.polls.views.vote'),
    (r'^mediafiles/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/silveira/Desktop/foiaqui/media'}),
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^crimes/xml', 'foiaqui.crimes.views.index'),
	(r'^crimes/insert', 'foiaqui.crimes.views.insert_incident'),
    (r'^$', 'foiaqui.core.views.index'),
#    (r'^contact/thankyou/', 'contacts.views.thankyou'),
#    (r'^contact/', 'contacts.views.contactview'),
)
