from django.conf.urls import patterns, url

from retreat_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^retreats/', views.retreats, name='retreats')

)

