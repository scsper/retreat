from django.conf.urls import patterns, url

from retreat_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^retreats/', views.retreats, name='retreats'),
    url(r'^login/', views.login_view, name='login_view'),
    url(r'^validate_login/', views.validate_login, name='validate_login'),


)

