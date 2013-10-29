from django.conf.urls import patterns, url

from pnm import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<pnmId>\d+)/$', views.detail, name='detail'),
)

