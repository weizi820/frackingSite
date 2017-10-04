from django.conf.urls import include, url
from  . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^awards/$', views.awards, name='awards'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^education/$', views.education, name='education'),
    url(r'^research_current/$', views.research_current, name='research_current'),
    url(r'^research/$', views.research, name='research'),
    url(r'^resume/$', views.resume, name='resume'),
	url(r'^skills/$', views.skills, name='skills'),
    url(r'^work/$', views.work, name='work'),
    url(r'', include('pkn.urls')),
]