__author__ = 'raymond'
from django.conf.urls import patterns, url

from Poll import views

urlpatterns = patterns('',
                       # ex: /polls/
                       url(r'^$', views.index, name='index'),
                       # ex: /polls/
                       url(r'^jsonIndex/$', views.jsonIndex, name='jsonIndex'),
                       # ex: /polls/5/
                       url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
                       url(r'^(?P<poll_id>\d+)/json/$', views.detailJson, name='detailJson'),
                       # ex: /polls/5/results/
                       url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
                       # ex: /polls/5/vote/
                       url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'))
