from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.sim_list, name='sim_list'),
	url(r'^sim/(?P<pk>\d+)/$', views.sim_detail, name='sim_detail'),
	url(r'^sim/new/$', views.sim_new, name='sim_new'),
	url(r'^sim/(?P<pk>\d+)/edit/$', views.sim_edit, name='sim_edit'),
	url(r'^drafts/$', views.sim_draft_list, name='sim_draft_list'),
	url(r'^sim/(?P<pk>\d+)/publish/$', views.sim_publish, name='sim_publish'),
	url(r'^sim/(?P<pk>\d+)/remove/$', views.sim_remove, name='sim_remove'), 
]