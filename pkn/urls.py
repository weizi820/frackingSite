from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^pkn/$', views.pkn_main, name='pkn_main'),
	url(r'^pkn/design/$', views.pkn_design, name='pkn_design'),
	url(r'^pkn/analysis/$', views.pkn_analysis, name='pkn_analysis'),
	url(r'^pkn/results/$', views.pkn_results, name='pkn_results'),
	url(r'^pkn/help/$', views.pkn_help, name='pkn_help'),	
	url(r'^pkn/list$', views.sim_list, name='sim_list'),	
	url(r'^pkn/sim/(?P<pk>\d+)/$', views.sim_detail, name='sim_detail'),
	url(r'^pkn/sim/new/$', views.sim_new, name='sim_new'),
	url(r'^pkn/sim/(?P<pk>\d+)/edit/$', views.sim_edit, name='sim_edit'),
	url(r'^pkn/drafts/$', views.sim_draft_list, name='sim_draft_list'),
	url(r'^pkn/sim/(?P<pk>\d+)/publish/$', views.sim_publish, name='sim_publish'),
	url(r'^pkn/sim/(?P<pk>\d+)/remove/$', views.sim_remove, name='sim_remove'), 
]