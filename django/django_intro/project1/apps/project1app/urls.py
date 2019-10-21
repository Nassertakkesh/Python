from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^bears$', views.one_method),  
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<numbs>[0-9]+)$', views.number),
    url(r'^(?P<numbs>[0-9]+)/edit$', views.edit),
    url(r'^(?P<numbs>[0-9]+)/delete$', views.destroy),
]
