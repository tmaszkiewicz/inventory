"""T3000 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.inventory import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'workstations/$', views.workstations, name="workstations"),
    url(r'servers/$', views.servers, name="servers"),
    url(r'summary/$', views.summary, name="summary"),
    url(r'winsvrlic/$', views.winsvrlic, name="winsvrlic"),
    url(r'officelic/$', views.officelic, name="officelic"),
    url(r'workstation_edit/(?P<pk>\d+)/$', views.workstation_edit, {},  name="workstation_edit"),
    url(r'workstations_export/$', views.workstations_export,  name="workstations_export"),
    url(r'winsvrlic_edit/(?P<pk>\d+)/$', views.winsvrlic_edit, {},  name="winsvrlic_edit"),
    url(r'winsvrlic_del/(?P<pk>\d+)/$', views.winsvrlic_del, {},  name="winsvrlic_del"),
    url(r'winsvrlic_new/$', views.winsvrlic_new,  name="winsvrlic_new"),
    url(r'officelic_new/$', views.officelic_new,  name="officelic_new"),
    url(r'officelic_edit/(?P<pk>\d+)/$', views.officelic_edit, {},  name="officelic_edit"),
    url(r'svr_edit/(?P<pk>\d+)/$', views.svr_edit, {},  name="svr_edit"),
    url(r'delete/$', views.delete_unrelated_users,  name="delete_unrelated_users"),
    url(r'users/$', views.users, name="users"),
    url(r'spot/$', views.spot, name="spot"),
    url(r'term_import/$', views.term_import,  name="term_import"),
    url(r'terminals/$', views.terminals, name="terminals"),
    url(r'term_edit/(?P<pk>\d+)/$', views.term_edit,  name="term_edit"),
   #url(r'kj/(?P<etykieta>[0-9]+)/(?P<dzial>[a-z]+)//$',  views.kj, name='kj'),
    url(r'kj/$', views.kj, name='kj'),
    url(r'form/(?P<event>\d+)', views.eventForm),    
    url(r'newevent/(?P<term>\d+)', views.newEventForm),    
    url(r'eventfilter/(?P<term>\d+)', views.eventFilter),    
    url(r'events/$', views.eventFilter,name="events"),
    url(r'terms_del/$', views.terms_del,name="terms_del"),
    #url(r'^login/$', auth_views.login, name='login'),
    url('accounts/', include('django.contrib.auth.urls')),
]
