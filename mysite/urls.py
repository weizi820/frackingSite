from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as django_views
from  . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   	url(r'^accounts/login/$', django_views.login, name='login'),
   	url(r'^accounts/logout/$', django_views.logout, name='logout', kwargs={'next_page': '/'}),
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