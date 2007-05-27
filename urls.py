from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^polls/$', 'fa.polls.views.index'),
    (r'^polls/(?P<poll_id>\d+)/$', 'fa.polls.views.detail'),
    (r'^polls/(?P<poll_id>\d+)/results/$', 'fa.polls.views.results'),
    (r'^polls/(?P<poll_id>\d+)/vote/$', 'fa.polls.views.vote'),
    (r'^admin/', include('django.contrib.admin.urls')),
)
