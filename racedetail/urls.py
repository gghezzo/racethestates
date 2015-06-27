from django.conf.urls import include, url
from . import views

#     

urlpatterns = [
    url(r'^$', views.race_list),
    url(r'^raceDetail/(?P<pk>[0-9]+)/$', views.race_detail),
    url(r'^raceDetail/new/$', views.race_new, name='race_new'),
    url(r'^raceDetail/(?P<pk>[0-9]+)/edit/$', views.race_edit, name='race_edit'),
]