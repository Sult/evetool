from django.conf.urls import patterns, url

from users import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^register/$', views.register_user, name='register_user'),
    # url(r'^register_succes/$', views.register_succes, name='register succes'),

    # #information pages
    # url(r'^contact/$', views.contact, name='contact'),
)
