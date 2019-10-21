from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.shows),
    url(r'^shows$', views.shows),
    url(r'^shows/(?P<id>\d+)$', views.shows_page),
    url(r'^shows/(?P<id>\d+)/edit$', views.edit_show),
    url(r'^shows/(?P<id>\d+)/delete$', views.delete_show),
    url(r'^shows/new$', views.new_show),
    url(r'^shows/addingnewshow$', views.add_new_show),
]