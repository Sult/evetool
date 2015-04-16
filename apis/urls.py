from django.conf.urls import patterns, url

from apis import views

urlpatterns = patterns(
    '',
    url(r'^APIs/$', views.apis, name='apis'),
    url(r'^API/update/(?P<pk>\d+)/$', views.update_api, name='update_api'),
    url(r'^API/delete/(?P<pk>\d+)/$', views.delete_api, name='delete_api'),
)
