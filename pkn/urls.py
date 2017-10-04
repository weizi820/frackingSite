from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as django_views
from . import views

urlpatterns = [
	url(r'^pkn/$', views.pkn_main, name='pkn_main'),
    url(r'^pkn/admin/', admin.site.urls),
   	url(r'^pkn/accounts/login/$', django_views.login, name='login'),
   	url(r'^pkn/accounts/logout/$', django_views.logout, name='logout', kwargs={'next_page': '/pkn/'}),
   	url(r'^pkn/accounts/signup/$', views.pkn_signup, name='pkn_signup'),
	url(r'^pkn/design/$', views.pkn_design, name='pkn_design'),
	url(r'^pkn/analysis/$', views.pkn_analysis, name='pkn_analysis'),
	url(r'^pkn/design/results/$', views.pkn_design_results, name='pkn_design_results'),
	url(r'^pkn/analysis/results/$', views.pkn_analysis_results, name='pkn_analysis_results'),
	url(r'^pkn/help/$', views.pkn_help, name='pkn_help'),
	url(r'^pkn/error/$', views.pkn_error, name='pkn_error'),	
	url(r'^pkn/list$', views.sim_list, name='sim_list'),	
	url(r'^pkn/drafts/$', views.sim_draft_list, name='sim_draft_list'),
	url(r'^pkn/sim/new/$', views.sim_new, name='sim_new'),
	url(r'^pkn/sim/(?P<pk>\d+)/$', views.sim_detail, name='sim_detail'),
	url(r'^pkn/sim/(?P<pk>\d+)/edit/$', views.sim_edit, name='sim_edit'),
	url(r'^pkn/sim/(?P<pk>\d+)/publish/$', views.sim_publish, name='sim_publish'),
	url(r'^pkn/sim/(?P<pk>\d+)/remove/$', views.sim_remove, name='sim_remove'), 
]