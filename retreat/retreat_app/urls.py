from django.conf.urls import patterns, url

from retreat_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^retreats/$', views.retreats, name='retreats'),
    # url(r'^validate_login/', views.validate_login, name='validate_login'),

    url(r'^accounts/login/$', views.login_view, name='login_view'),
    url(r'^accounts/auth/$', views.auth_view, name='auth_view'),
    # url(r'^accounts/logout/$', views.logout, name='logout'),
    # url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/invalid/$', views.invalid, name='invalid'),

    url(r'^retreats/(?P<retreat_id>\d+)/$', views.retreat_view, name="retreat_view"),
    url(r'^retreats/(?P<retreat_id>\d+)/roster/$', views.roster_view, name="roster_view")


)
