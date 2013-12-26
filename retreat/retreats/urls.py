from django.conf.urls import patterns, url

from retreats import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)